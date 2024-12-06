import streamlit as st
import os

from langchain_openai.chat_models import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from llm_model import llm
from userstories_template import user_stories,extract_json,code_gen,userstories_microservice_prompt,javacode_prompt
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import JsonOutputParser
from util import extract_code, get_code_prompt, safe_write
from chains import (
    product_manager_chain,
    tech_lead_chain,
    test_lead_chain,
    file_structure_chain,
    file_path_chain,
    code_chain,
    missing_chain,
    new_classes_chain
)
import tiktoken

def count_tokens(text, model="gpt-4o"):
    # Load the tokenizer for the specified model
    encoding = tiktoken.encoding_for_model(model)
    # Encode the text and count tokens
    tokens = encoding.encode(text)
    return len(tokens)


    
   
@st.cache_data(show_spinner="Extracting Json Values...")
def extract_json_obj(exec_prompt,response,model):    
    final_prompt = PromptTemplate.from_template(exec_prompt)
    # formatted_prompt = final_prompt.format(text=response)
    llm_instance = llm(model)  
    parser = JsonOutputParser()
    chain =final_prompt | llm_instance | parser
    result = chain.invoke({"text": response})
    return result

@st.cache_data(show_spinner="Mapping the user stories with the respective microservices")
def usertoriesmapping(userstories_mapping_prompt, oo_design_response, json_output,model_name="gpt-4o"):    
    memory = ConversationBufferMemory(return_messages=True)    
    parser = JsonOutputParser()
    conversation = ConversationChain(llm=llm(model_name=model_name), memory=memory)
    final_prompt = PromptTemplate.from_template(userstories_mapping_prompt)
    formatted_prompt = final_prompt.format(microservice_design=oo_design_response,user_stories=json_output)  
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
    json_response = parser.parse(full_response)      
    return json_response

#Previous Versions -----------------------------------------------------------------
# @st.cache_data(show_spinner="Generating userstories...")
# def userstories_x(exec_prompt, code,model_name):   
#     memory = ConversationBufferMemory(return_messages=True)    
#     conversation = ConversationChain(llm=llm(model_name=model_name), memory=memory)
#     final_prompt = PromptTemplate.from_template(exec_prompt)
#     formatted_prompt = final_prompt.format(PLSQL_CODE=code)    
#     response = conversation.predict(input=formatted_prompt)
#     full_response = response
#     max_tokens = 500
#     needs_continuation = len(response.split()) >= max_tokens - 50
#     count = 0
#     while needs_continuation and count<=5:
#         continuation_prompt = "Please continue where you left.."
#         continuation_response = conversation.predict(input=continuation_prompt)
#         full_response += " " + continuation_response
#         needs_continuation = len(continuation_response.split()) >= max_tokens - 50
#         count+=1
#         # st.write(memory.load_memory_variables({}))
#     return full_response

    # final_prompt = PromptTemplate.from_template(exec_prompt)
    # formatted_prompt = final_prompt.format(PLSQL_CODE=code)
    # llm_instance = llm(model_name)  # Create the LLM instance
    # response = llm_instance.predict(formatted_prompt)
    # for chunk in llm_instance.stream(formatted_prompt):
    #     st.write(chunk.content, end=" ")
    # return response

@st.cache_data(show_spinner="Generating userstories...")
def userstories(exec_prompt, code,model_name):   
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

@st.cache_data(show_spinner="Generating userstories...")
def userstories_microservice(exec_prompt,response,model_name,code): 
    parser = JsonOutputParser()  
    memory = ConversationBufferMemory(return_messages=True)    
    conversation = ConversationChain(llm=llm(model_name=model_name), memory=memory)
    final_prompt = PromptTemplate.from_template(exec_prompt)
    formatted_prompt = final_prompt.format(USER_STORIES =response,PLSQL_CODE=code)  
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
    full_response_json = parser.parse(full_response)    
    return full_response_json

# @st.cache_data(show_spinner="Generating the java code...")
# def getjavacode_new(exec_prompt,userstories,model_name,plsql_str):   
#     memory_code = ConversationBufferMemory(return_messages=True)    
#     conversation_chain = ConversationChain(
#         llm=llm(model_name=model_name),
#           memory=memory_code)
#     final_prompt = PromptTemplate.from_template(exec_prompt)    
#     full_response =""
    
#     for i in range(len(userstories)):        
#         formatted_prompt = final_prompt.format(user_stories=userstories[i])
#         response = conversation_chain.predict(input=formatted_prompt)
#         # Initialize the full response..        
#         full_response += " " + response
#         print("For Loop -> ",i)
#         encoding = tiktoken.encoding_for_model("gpt-4o")
#         tokens = encoding.encode(full_response)
#         print("--> Number of tokens:", len(tokens))
#     with st.expander('memeorycheck'):
#         st.write(memory_code.load_memory_variables({}))
#     return full_response 
        


# @st.cache_data(show_spinner="Generating the java code...")
# def getjavacode_new(userstories):    
#     for i in range(len(userstories)):        
#         st.write(userstories[i]['title'])
#         create_java_code(language="Java",app_name=str(userstories[i]['title']),request=str(userstories[i]))


# @st.cache_data(show_spinner="Generating the java code...")
def getjavacode_new(oo_json_output,mapping_result):
    values = (dict(list(oo_json_output.items())[:2]))

    for key_idx,v in values.items():
        # st.write(k)
        # st.write(oo_json_output[k])
        # if k in mapping_result:
        #     st.write(mapping_result[k])
        # else:
        #     st.write("No User Stories found for this microservice")     

        #--------------------------------
        final_prompt = PromptTemplate.from_template(javacode_prompt)
        formatted_prompt = final_prompt.format(microservice_design=oo_json_output[key_idx],userstories=mapping_result[key_idx])
        # st.divider()
        # st.write(formatted_prompt)
        create_java_code(language="Java",app_name=str(key_idx),request=formatted_prompt) 
        #-----------------------------------


def create_java_code(language ,app_name ,request = userstories ):
    dir_path = app_name + '/'

    requirements = product_manager_chain.run(request)
    req_doc_path = dir_path + '/requirements' + '/requirements.txt'
    safe_write(req_doc_path, requirements)
    # st.markdown(''' :blue[Business Requirements : ] ''', unsafe_allow_html=True)
    # st.write(requirements)

    tech_design = tech_lead_chain.run({'language': language, 'input': request})
    tech_design_path = dir_path + '/tech_design' + '/tech_design.txt'
    safe_write(tech_design_path, tech_design)
    st.markdown(''' :blue[Technical Design :] ''', unsafe_allow_html=True)
    st.write(tech_design)

    test_plan = test_lead_chain.run(requirements)
    test_plan_path = dir_path + '/test_plan' + '/test_plan.txt'
    safe_write(test_plan_path, test_plan)
    # st.markdown(''' :blue[Test Plan :] ''', unsafe_allow_html=True)
    # st.write(test_plan)

    file_structure = file_structure_chain.run({'language': language, 'input': tech_design})
    file_structure_path = dir_path + '/file_structure' + '/file_structure.txt'
    safe_write(file_structure_path, file_structure)
    st.markdown(''' :blue[File Names :] ''', unsafe_allow_html=True)
    st.write("*"*100)
    st.write(file_structure)
    st.write("*"*100)
    

    files = file_path_chain.run({'language': language, 'input': file_structure})
    files_path = dir_path + '/files' + '/files.txt'
    safe_write(files_path, files)
    # st.markdown(''' :blue[File Paths :] ''', unsafe_allow_html=True)
    # st.write("*"*100)
    # st.write(files)
    # st.write("*"*100)

    files_list = files.split('\n')

    missing = True
    missing_dict = {
        file: True for file in files_list
    }

    code_dict = {}

    while missing:

        missing = False
        new_classes_list = []

        for file in files_list:

            code_path = os.path.join(dir_path, 'code', file)
            norm_code_path = code_path

            if not missing_dict[file]:
                safe_write(norm_code_path, code_dict[file])
                st.markdown(''' :red[Code & Unit Tests: 2nd Iteration] ''', unsafe_allow_html=True)
                st.write(code_dict[file])
                continue

            code = code_chain.predict(
                language=language,
                class_structure=tech_design,
                structure=file_structure,
                file=file,
            )

            code_dict[file] = code
            
            response = missing_chain.run({'language': language, 'code': code})
            if '<TRUE>' in response:
                missing = missing or missing_dict[file]
            else:
                safe_write(norm_code_path, code)
                st.markdown(''' :blue[Complete Code & Unit Tests: 1st Iteration] ''', unsafe_allow_html=True)
                st.write(code)
                continue

            if missing_dict[file]:
                new_classes = new_classes_chain.predict(
                    language=language,
                    class_structure=tech_design,
                    code=code
                )
                new_classes_list.append(new_classes)

        tech_design += '\n\n' + '\n\n'.join(new_classes_list)


def create_user_stories(code):    
    # with st.expander("User Stories"):
    # model_name = st.radio(label="Select the models",options =["gpt-4o","gpt-4o-mini","o1-preview"])
    response =userstories(user_stories, code,model_name="o1-preview")
    final_output = userstories_microservice(userstories_microservice_prompt,response,model_name="o1-preview",code=code)
    st.write("Check the Token Count")
    st.success(f"Token Count {count_tokens(response)}")
    return response,final_output

def get_json(result):   
    result = extract_json_obj(exec_prompt=extract_json,response=result,model="gpt-4o")
    st.success("Json Value Extracted Successfully..")
    return result



