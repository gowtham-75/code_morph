import streamlit as st
st.set_page_config(
    page_title="Code convertor",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded",
)

import os
import zipfile

from util import extract_code, get_code_prompt
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import AzureChatOpenAI
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from prompt_templates import code_explain_prompt, java_code_gen_prompt, oo_design_prompt,mermaid_code,Bl_logic,Fun_doc,duplicate_redundant,Techenical,Func_overview
from mermaid import (generateDiagram,
                     generate_mermaid_process_flow_chart,
                     generateDiagram1,
                     generate_mermaid_process_flow_chart_TD,
                     generate_mermaid_process_flow_chart_TD_graph,
                     generate_mermaid_process_flow_chart_graph,
                     generate_mermaid_component
                     )
import streamlit.components.v1 as components
from mermaid_prompt import mermaid_code_generate,sequence_diagram,Mindmap,ER_Diagram,State_Diagram,class_diagram,Flowchart
import time
load_dotenv()
from llm_model import llm, llm_Normal
from generatecode import create_user_stories,get_json,get_code
import re
import json
import pandas as pd
import pandas as pd
from langchain_core.output_parsers import JsonOutputParser
from pdf import pdf_convertion, pdf_convertion_with_mermaid


code_dir_name = "./code"
sql_dir_name = "./sql_files"
model_name = "gpt-4o"


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
        st.title('Code Converter')
        st.image("image/legacy_mod.jpeg", width=250)
        st.markdown("### About:")                                                                              
        st.markdown('<div style="text-align: justify;">The application leverages Generative AI to streamline the transformation of legacy PLSQL code into modern development artifacts.<br> This enables developers to expedite modernization efforts, ensure consistent documentation, and maintain clarity in codebase transitions.</div><br>', unsafe_allow_html=True)

def execute(exec_prompt, code):
    """
    Execute LLM with provided prompt template
    """
    final_prompt = PromptTemplate.from_template(exec_prompt)
    formatted_prompt = final_prompt.format(PLSQL_CODE=code)
    llm_instance = llm(formatted_prompt,model_name)  # Create the LLM instance
    return llm_instance


def get_mermaid_code(exec_prompt, code, value):
    """
    Execute LLM with provided prompt template
    """
    
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
    llm_instance = llm_Normal(model_name)  # Initialize your LLM here
    return llm_instance.predict(formatted_prompt)



# Cached function to get Mermaid code
@st.cache_data(show_spinner="Generate Diagram...")
def get_diagram_responses(diagram_prompt, code_text, diagram_type):
    # Fetch the mermaid code using the provided inputs
    return get_mermaid_code(diagram_prompt, code_text, diagram_type)

# Function to display the diagram
def display_diagram_option(diagram_prompt, diagram_type, code_text):
    # Initialize session state variable if not already set
    if "dig" not in st.session_state:
        st.session_state.dig = ""

    # Get responses (cached data)
    responses = get_diagram_responses(diagram_prompt, code_text, diagram_type)

    
    # Update session state
    st.session_state.dig = responses
    response = st.session_state.dig

    # Clean response for rendering
    cleaned_code = re.sub(r"^\n|```", "", response.strip())
    cleaned_code = re.sub(r"^mermaid", "", cleaned_code.strip())

    # Widget to display Mermaid diagram code
    mermaid_diagram_code = st.text_area("Enter Mermaid Diagram Code", value=cleaned_code, height=400)

    # Expander for Mermaid Diagram Code
    with st.expander("Mermaid Diagram Code"):
        st.code(mermaid_diagram_code, language="mmd")

    # Generate and display the diagram
    result = generateDiagram(mermaid_diagram_code)
    with st.expander("Mermaid Diagram"):
        st.components.v1.html(result, height=450)

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
    

def extract_sql_files(zip_path, sql_dir_name="sql_files"):
    # Create the SQL files directory if it doesn't exist
    os.makedirs(sql_dir_name, exist_ok=True)
    sql_files_content = {}
    code_text = ""
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_name in zip_ref.namelist():
            # Check if the file is a .pks or .pkb file
            if file_name.endswith('.pks') or file_name.endswith('.pkb') or file_name.endswith('.PKS') or file_name.endswith('.PKB'):
                # Extract each file to the specified directory
                zip_ref.extract(file_name, sql_dir_name)
                
                # Read the content of the file to store it (optional)
                with zip_ref.open(file_name) as file:
                    sql_files_content[file_name] = file.read().decode('utf-8')
                
                with zip_ref.open(file_name) as file:
                    code_text += f"__________{file.name}__________\n"
                    code_text += file.read().decode('utf-8')
                    code_text += "\n\n"
    
    return sql_files_content, code_text



def mermaid_diagram(response):
    html_string=""
    if 'flowchart LR' in response:
        code_diagram =generate_mermaid_process_flow_chart(response)
        for item in code_diagram:                     
            data_diagram = f""" flowchart LR \n {item}"""                        
            html_string = generateDiagram1(data_diagram)
        return html_string,data_diagram
            
    elif 'flowchart TD' in response:
        code_diagram = generate_mermaid_process_flow_chart_TD(response)
        for item in code_diagram:                     
            data_diagram = f""" flowchart TD \n {item}"""                        
            html_string = generateDiagram1(data_diagram)
        return html_string,data_diagram
    
    elif 'graph LR' in response:
        code_diagram =generate_mermaid_process_flow_chart_graph(response)
        for item in code_diagram:                     
            data_diagram = f""" graph LR \n {item}"""                        
            html_string = generateDiagram1(data_diagram)
        return html_string,data_diagram
    
    elif 'graph TD' in response:
        code_diagram = generate_mermaid_process_flow_chart_TD_graph(response)
        for item in code_diagram:                     
            data_diagram = f""" graph TD \n {item}"""                        
            html_string = generateDiagram1(data_diagram)
        return html_string,data_diagram
    
    elif 'componentDiagram' in response:
        code_diagram = generate_mermaid_component(response)
        for item in code_diagram:                     
            data_diagram = f""" componentDiagram \n {item}"""                        
            html_string = generateDiagram1(data_diagram)
        return html_string,data_diagram
    
    return("_")
    
          
            

def main():    
    hide_decoration_bar_style = '''<style> header {visibility: hidden;} </style>'''
    global json_output
    json_output = None
    # st.set_page_config(page_title="Code Morph", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
    st.title("Code Convertor")
    sidebar()
    # Tabs in the main view
    view, doc, diagram, userstories_gen,view_userstories ,code_gen = st.tabs(["Code View", "Document View", "UML Diagrams generator", "User Stories Generations","View UserStories" ,"Code Generator"])
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
            st.write("File path : ",zip_path)
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
        if 'doc0' not in st.session_state:
            st.session_state.doc0 = ""
        if 'doc1' not in st.session_state:
            st.session_state.doc1 = ""
        if 'doc2' not in st.session_state:
            st.session_state.doc2 = ""
        if 'doc3' not in st.session_state:
            st.session_state.doc3 = ""
        if 'doc4' not in st.session_state:
            st.session_state.doc4 = ""
        if 'doc5' not in st.session_state:
            st.session_state.doc5 = ""
        if 'doc6' not in st.session_state:
            st.session_state.doc6 = "" 
        if 'dig1' not in st.session_state:
            st.session_state.dig1 = ""
        if 'dig_data' not in st.session_state:
            st.session_state.dig_data = "" 
        if 'dig_oo' not in st.session_state:
            st.session_state.dig_oo = ""
        if 'dig_data_oo' not in st.session_state:
            st.session_state.dig_data_oo = ""
        if 'dig_bu' not in st.session_state:
            st.session_state.dig_bu = ""
        if 'dig_data_bu' not in st.session_state:
            st.session_state.dig_data_bu = ""        
        
        enable = st.toggle("Enable Document Explain")
        if sql_files_content and enable:
            col1, col2 = st.columns([1, 3])
            with col1:
                selected_option = st.radio("Select the operations : ",options=["Function Document overview","Functional Document","Business Document","Technical Document","PLSQL Code Explain","Identify Duplicate and Redundant code","Generate Java OO Design​"],horizontal=False)
            with col2:
                if selected_option == "Functional Document":
                    st.write("## Functional Document")
                    # st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
                    if not st.session_state.doc0:
                        response = execute(Fun_doc, code_text)
                        st.session_state.doc0 = response                    
                    pdf_convertion(st.session_state.doc0)
                    st.write(st.session_state.doc0)
                    
                
                # Generate and store response in session_state based on selected option
                elif selected_option == "PLSQL Code Explain":
                    st.write("## PLSQL Code Explain")
                    if not st.session_state.doc1:  # Check if response already exists in session_state
                        response = execute(code_explain_prompt, code_text)
                        st.session_state.doc1 = response  # Store response in session_state
                    st.write(st.session_state.doc1)  # Display the stored response

                elif selected_option == "Business Document":
                    st.write("## Business Document")
                    if not st.session_state.doc2:
                        response = execute(Bl_logic, code_text)
                        st.session_state.doc2 = response
                    st.session_state.dig_bu,st.session_state.dig_data_bu=mermaid_diagram(st.session_state.doc2)

                    pdf_convertion_with_mermaid(st.session_state.doc2,st.session_state.dig_data_bu) 
                    st.write(st.session_state.doc2) 
                    components.html(st.session_state.dig_bu, height=400, scrolling=True)

                elif selected_option == "Identify Duplicate and Redundant code":
                    st.write("## Identify duplicate and redundant")
                    if not st.session_state.doc4:
                        response = execute(duplicate_redundant, code_text)
                        st.session_state.doc4 = response
                    st.write(st.session_state.doc4)
                    
                elif selected_option == "Generate Java OO Design​":
                    st.write("## Generate Java Object Oriented Design")
                    if not st.session_state.doc3:
                        response = execute(oo_design_prompt, code_text)
                        st.session_state.doc3 = response
                    st.session_state.dig_oo,st.session_state.dig_data=mermaid_diagram(st.session_state.doc3)

                    pdf_convertion_with_mermaid(st.session_state.doc3,st.session_state.dig_data_oo) 
                    st.write(st.session_state.doc3) 
                    components.html(st.session_state.dig_oo, height=400, scrolling=True)
                    
                    
                elif selected_option == "Technical Document":
                    st.write("## Technical Document")
                    if not st.session_state.doc5:
                        response = execute(Techenical, code_text)
                        st.session_state.doc5 = response
                    pdf_convertion(st.session_state.doc5)
                    st.write(st.session_state.doc5)
                                    
                elif selected_option == "Function Document overview":
                    st.write("## Function Document overview")
                    if not st.session_state.doc6:
                        response = execute(Func_overview, code_text)
                        st.session_state.doc6 = response
                    
                    st.session_state.dig1,st.session_state.dig_data=mermaid_diagram(st.session_state.doc6)

                    pdf_convertion_with_mermaid(st.session_state.doc6,st.session_state.dig_data) 
                    st.write(st.session_state.doc6) 
                    components.html(st.session_state.dig1, height=400, scrolling=True)

                   
                    
        else:
            st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")

        
    
    # with diagram:
        
    #     st.header("Generate UML Diagram")
    #     enable_diagram = st.toggle("Enable Generate options")
    #     if sql_files_content and enable_diagram:
    #         main_diagram_tab(code_text)
    #     # elif sql_files_content is not None and  enable_diagram == False:
    #     #     st.success("sql files found..")
    #     #     st.warning("Click the Enable toggle and continue..")
    #     else:
    #         st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")
    
        

    # with userstories_gen:
    #     st.header("Generate userstories")
    #     enable_option=st.toggle("Enable User Stories")
    #     if sql_files_content and enable_option:
    #         plsql_result,java_result = create_user_stories(code=code_text)
    #         with st.expander("PLSQL Code -> Plsql User Stories"):
    #             st.write(plsql_result)
            
    #         with st.expander("Plsql User Stories-->Java Microservice User Stories"):
    #             st.write(java_result)
    #         if java_result:
    #             json_output=get_json(java_result)
    #             # with st.expander("User Stories JSON"):
    #             #     st.code(json_output,language="json")
    #         else:
    #             json_output = None
      
    #     else:
    #         st.warning("No SQL files found in the uploaded zip file. Please upload a zip file containing SQL files.")
            

    # with view_userstories:
    #     st.header("View User Stories")
    #     if json_output is not None:
    #         # st.write(len(json_output))
    #         data = pd.DataFrame(json_output)
    #         st.dataframe(data, use_container_width=True,hide_index=True)
    #         # input = st.number_input("Enter the number of user stories to display", min_value=1)
    #         if st.toggle('generate the Code'):
    #             code_result=get_code(json_output,code =code_text,plsql_str=java_result)
    #             st.code(code_result,language="java")

            
            # for i in range(len(json_output)):
            #     st.write(json_output[i]["id"])
            #     st.write(json_output[i]["title"])
            #     st.write(json_output[i]["acceptance_criteria"])
            #     st.write(json_output[i]["requirements"])


                
            # st.write(json_output[0]["description"])
            # st.write(json_output[0]["id"])     

        # else:
        #     st.warning("No User Stories found. Please generate user stories first.")

    # with code_gen:
    #     st.header("Code generator")
 

if __name__ == '__main__':
    main()
