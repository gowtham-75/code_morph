import streamlit as st
import os
import zipfile
from llm_model import llm
from util import extract_sql_files
from generatecode import create_user_stories,get_json,getjavacode_new,usertoriesmapping,extract_json_obj
import re
from langchain_core.output_parsers import JsonOutputParser
import chains
import tiktoken
import pandas as pd
from dotenv import load_dotenv
import json
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import AzureChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from prompt_templates import code_explain_prompt, java_code_gen_prompt, oo_design_prompt,mermaid_code,Bl_logic
from mermaid import (generateDiagram,
                     generate_mermaid_process_flow_chart,
                     generateDiagram1,
                     generate_mermaid_process_flow_chart_TD)
from langchain_core.prompts import PromptTemplate
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from userstories_template import oo_design_prompt_plus,userstories_mapping_prompt,extract_oo_design_json
import streamlit.components.v1 as components
from mermaid_prompt import mermaid_code_generate,sequence_diagram,Mindmap,ER_Diagram,State_Diagram,class_diagram,Flowchart
import time
load_dotenv()


code_dir_name = "./code"
sql_dir_name = "./sql_files"
model_name = "gpt-4o"
AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
DEPLOYMENT_NAME = os.environ['DEPLOYMENT_NAME']

gpt_4o = AzureChatOpenAI(azure_deployment=DEPLOYMENT_NAME,  
    api_key=AZURE_OPENAI_API_KEY,          
    azure_endpoint=AZURE_ENDPOINT,  
    api_version="2023-09-01-preview" ,
    temperature=0.5,
    model="gpt-4o",
    max_tokens = 4000,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()])

gpt_4o_mini =AzureChatOpenAI(azure_deployment=DEPLOYMENT_NAME,  
    api_key=AZURE_OPENAI_API_KEY,          
    azure_endpoint=AZURE_ENDPOINT,  
    api_version="2023-09-01-preview" ,
    temperature=0.5,
    model="gpt-4o-mini",
    max_tokens = 4000,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()])

def sidebar():
    st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width:300px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
    )
    with st.sidebar:
        st.title('CodeMorph_AI')
        st.image("image/legacy_mod.jpeg", width=295)
        # add_radio = st.radio(
        #     'Select the LLM to be used!',
        #     ('openai-gpt-4o',
        #     'openai-gpt_4o_mini'))

        # if add_radio == 'openai-gpt-4o':
        #     chains.set_llm(gpt_4o)
        # elif add_radio == 'openai-gpt_4o_mini':
        #     chains.set_llm(gpt_4o_mini)


def execute(exec_prompt, code):
    """
    Execute LLM with provided prompt template
    """
    final_prompt = PromptTemplate.from_template(exec_prompt)
    formatted_prompt = final_prompt.format(PLSQL_CODE=code)
    llm_instance = llm(model_name)  # Create the LLM instance
    return llm_instance.predict(formatted_prompt)

@st.cache_data(show_spinner="Generate the OO Design")
def execute_plus(exec_prompt, code,model_name="gpt-4o"):   
    memory = ConversationBufferMemory(return_messages=True)    
    conversation = ConversationChain(llm=llm(model_name=model_name), memory=memory)
    final_prompt = PromptTemplate.from_template(exec_prompt)
    formatted_prompt = final_prompt.format(PLSQL_CODE=code)  
    response = conversation.predict(input=formatted_prompt)    
    # Initialize the full response
    full_response = response   
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode(full_response)
    st.write("--> Number of tokens:", len(tokens))
    max_tokens = 4000
    needs_continuation = len(tokens) >= max_tokens - 600
    while needs_continuation:
        continuation_prompt = "Please continue where you left off."
        continuation_response = conversation.predict(input=continuation_prompt)
        full_response += " " + continuation_response
        tokens_continuation = encoding.encode(continuation_response)
        needs_continuation = len(tokens_continuation) >= max_tokens - 600     
        # st.write(continuation_response)
        # Add a safeguard to prevent infinite loops
        if len(full_response) > max_tokens * 5:
            st.write(f"Full Response -> {len(full_response)}\nMax token {max_tokens*5}")
            st.write("Reached maximum token limit. Stopping continuation.")  # Limit to 5 continuations
            break          
    return full_response




def get_mermaid_code(exec_prompt, code, value):
    """
    Execute LLM with provided prompt template
    """
    # # Debugging: Print values to check placeholders
    # print("exec_prompt:", exec_prompt)
    # print("code:", code)
    # print("value:", value)
    
    # Check for placeholders in the prompt template
    if '{PLSQL_CODE}' not in exec_prompt or '{UML_DIAGRAM}' not in exec_prompt:
        raise st.write(ValueError("exec_prompt must contain {PLSQL_CODE} and {UML_DIAGRAM} placeholders."))
    
    # Create and format the prompt
    final_prompt = PromptTemplate.from_template(exec_prompt)
    try:
        formatted_prompt = final_prompt.format(PLSQL_CODE=code, UML_DIAGRAM=value)
    except KeyError as e:
        st.write("KeyError:", e)  # Print exact missing key
        raise

    # Ensure `llm_instance` is initialized correctly
    llm_instance = llm(model_name)  # Initialize your LLM here
    return llm_instance.predict(formatted_prompt)




def display_diagram_option(diagram_prompt,diagram_type, code_text):
    response = get_mermaid_code(diagram_prompt, code_text, diagram_type)
    cleaned_code = re.sub(r"^\n|```", "", response.strip())
    cleaned_code = re.sub(r"^mermaid","",cleaned_code.strip())    
    with st.expander("Mermaid Diagram Code"):
        mermaid_diagram_code = st.text_area("Enter Mermaid Diagram Code", value=cleaned_code,)
        st.code(mermaid_diagram_code,language="mmd")
    # Generate Diagram
    if st.button(f"Generate {diagram_type}"):        
        result = generateDiagram(mermaid_diagram_code)
        return st.components.v1.html(result,height=2000)


def main_diagram_tab(code_text):
    st.header("Generate UML Diagram")
    col1, col2 = st.columns([1, 3])
    with col1:
        selected_option = st.radio(
            "Select the Diagram option to Generate:", 
            options=["Class diagram", "Sequence diagram", "ER diagram", "State Diagram", "Mindmap diagram","Flow Diagram"],
            horizontal=False
        )    
    with col2:        
        # if selected_option == "Class diagram":
        #     # class_diagram = "Code: {PLSQL_CODE} | Diagram Type: {UML_DIAGRAM}"
        if selected_option == "Class diagram":
            # class_diagram = "Code: {PLSQL_CODE} | Diagram Type: {UML_DIAGRAM}"
            uml_propmt = class_diagram
        elif selected_option == "Sequence diagram":
            uml_propmt = sequence_diagram           
        elif selected_option ==  "ER diagram":
            uml_propmt =ER_Diagram
        elif selected_option == "State Diagram":
            uml_propmt = State_Diagram
        elif selected_option == "Mindmap diagram":
            uml_propmt = Mindmap
        elif selected_option == "Flow Diagram":
            uml_propmt = Flowchart   
        return display_diagram_option(uml_propmt,selected_option, code_text)
    

def parse_to_json(response_text):
    try:
        parsed_response = json.loads(response_text)
        return parsed_response
    except json.JSONDecodeError:
        st.write("Error: The response is not in valid JSON format.")
        return None



        



def main():    
    global json_output,mapping_result,oo_json_output
    mapping_result=None
    json_output = None
    oo_json_output = None
    st.set_page_config(page_title="Code Morph", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.title("CodeMorph_AI")
    sidebar()
    # Tabs in the main view
    view, doc, diagram, OO_desgin,userstories_gen,view_userstories ,code_gen = st.tabs(["Code View", "Document View", "UML Diagrams generator", "OO Design","User Stories generator","Generate JAVA Code " ,"Code Generator"])
    sql_files_content = {}
    with view:
        st.header("Code View")
        # ------------------------------------------------------------------------------------------------------
        file = st.file_uploader("Upload the Zip files", type=['zip'], accept_multiple_files=False)
        # file_path = st.text_input("Enter the file path:")
        file_path = None
        if file is not None and file_path is None:
            file_details = {"FileName": file.name, "FileType": file.type}
            # st.write(file_details)
            zip_path = os.path.join(code_dir_name, file.name)
            with open(zip_path, "wb") as f:
                f.write(file.getvalue())
            st.write(zip_path)
            sql_files_content,code_text = extract_sql_files(zip_path)
            if sql_files_content:
                with st.expander("Code View"):                  
                        for name,file in sql_files_content.items():
                            st.subheader(f"Contents of {name}")
                            st.code(sql_files_content[name], language='sql')
            else:
                st.warning("No SQL files found in the uploaded zip file.")
        else:
            st.warning("Please upload a zip file.")

    with doc:
        st.header("Document Explain")
        enable = st.checkbox("Enable Document Explain")
        if sql_files_content and enable:
            col1, col2 = st.columns([1, 3])
            with col1:
                selected_option = st.radio("Select the operations : ",options=["PLSQL Code Explain","Business case Explain","Generate Java OO Design​"],horizontal=False)
            with col2:
                if selected_option == "PLSQL Code Explain":
                    st.write("PLSQL Code Explain")
                    for file in sql_files_content:
                        # print("content of the file is: ", code_text)
                        response = execute(code_explain_prompt, code_text)
                        st.write(response)
                   
                elif selected_option == "Business case Explain":
                    st.write("Business case Explain")
                    response = execute(Bl_logic, code_text)
                    st.write(response)
                    
                elif selected_option == "Generate Java OO Design​":
                    st.write("Generate Java OO Design​")
                    response = execute_plus(oo_design_prompt, code_text)
                    st.write(response)
                    
                    if 'flowchart LR' in response:
                        code_diagram =generate_mermaid_process_flow_chart(response)
                        for item in code_diagram:                     
                            data_diagram = f""" flowchart LR \n {item}"""                        
                            html_string = generateDiagram1(data_diagram)
                        
                            components.html(html_string, height=400, scrolling=True)
                    elif 'flowchart TD' in response:
                        code_diagram = generate_mermaid_process_flow_chart_TD(response)
                        for item in code_diagram:                     
                            data_diagram = f""" flowchart TD \n {item}"""                        
                            html_string = generateDiagram1(data_diagram)
                            components.html(html_string, height=400, scrolling=True)
                    else:
                        html_string = generateDiagram1(response)
                        components.html(html_string, width=900,height=450, scrolling=True)
                    
        else:
            st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")

        

    with diagram:
        
        st.header("Generate UML Diagram")
        enable_diagram = st.checkbox("Enable Generate options")
        if sql_files_content and enable_diagram:
            main_diagram_tab(code_text)
        # elif sql_files_content is not None and  enable_diagram == False:
        #     st.success("sql files found..")
        #     st.warning("Click the Enable Checkbox and continue..")
        else:
            st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")
    
        
    with OO_desgin:
        st.header("Generate OO Design")
        enable_OO = st.toggle("Enable OO Design")
        if sql_files_content and enable_OO:
            oo_design_response = execute_plus(oo_design_prompt_plus, code_text)
            st.write(oo_design_response)
            oo_json_output= extract_json_obj(exec_prompt=extract_oo_design_json,response=oo_design_response,model="gpt-4o")
            with st.expander("Microservice Design JSON"):
                st.write(oo_json_output)
            
            

        else:
            st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")
    with userstories_gen:
        st.header("Generate userstories")
        enable_option=st.toggle("Enable User Stories")
        if sql_files_content and enable_option:
            plsql_result,java_result = create_user_stories(code=code_text)
            with st.expander("PLSQL Code -> Plsql User Stories"):
                st.write(plsql_result)
            
            with st.expander("Plsql User Stories-->Java Microservice User Stories"):
                st.write(java_result)
            if java_result:
                json_output = java_result
                # json_output=get_json(java_result)
                # with st.expander("User Stories JSON"):
                #     st.code(json_output,language="json")
            else:
                json_output = None

            with st.expander("Mapping the Microservice with userstories"):
                if json_output is not None and oo_json_output is not None:
                    mapping_result=usertoriesmapping(userstories_mapping_prompt, oo_design_response, json_output)
                    for key_idx,val_idx in mapping_result.items():
                        st.write(f"**{key_idx}**")
                        for value in range(len(mapping_result[key_idx])):
                            st.write(" - {}".format(mapping_result[key_idx][value]['title']))
                    # st.write(type(mapping_result))
                    # for key,val in mapping_result.items():
                    #     print(key,val)


                elif json_output is None:
                    mapping_result=None
                    st.warning("No User Stories found. Please generate user stories first.")
                elif oo_design_prompt is None:
                    mapping_result=None
                    st.warning("No OO Design found. Please generate OO Design first.")       
                
            
        else:
            st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")
            

    with view_userstories:
        add_radio = st.radio(
            'Select the LLM to be used!',
            ('openai-gpt-4o',
            'openai-gpt_4o_mini'))

        if add_radio == 'openai-gpt-4o':
            chains.set_llm(gpt_4o)
        elif add_radio == 'openai-gpt_4o_mini':
            chains.set_llm(gpt_4o_mini)

        st.header("Generate JAVA Code")
        if mapping_result is not None and oo_json_output is not None:       
            # st.write(len(json_output))
            
            if st.toggle('generate the Code'):
                getjavacode_new(oo_json_output,mapping_result)
   
            #     st.code(code_result,language="java")
            
            # for i in range(len(json_output)):
            #     st.write(json_output[i]["id"])
            #     st.write(json_output[i]["title"])
            #     st.write(json_output[i]["acceptance_criteria"])
            #     st.write(json_output[i]["requirements"])


                
            # st.write(json_output[0]["description"])
            # st.write(json_output[0]["id"])           
            
            
                        
           
            

        else:
            st.warning("No User Stories found. Please generate user stories first.")

    with code_gen:
        st.header("Code generator")   
        
        
if __name__ == '__main__':
    main()
