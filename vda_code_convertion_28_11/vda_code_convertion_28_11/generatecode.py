import streamlit as st
import os

from langchain_openai.chat_models import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from llm_model import llm, llm_Normal
from userstories_template import user_stories,extract_json,code_gen,userstories_microservice_prompt
from dotenv import load_dotenv
load_dotenv()
from langchain_core.output_parsers import JsonOutputParser

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
    formatted_prompt = final_prompt.format(text=response)
    llm_instance = llm_Normal(model)  
    parser = JsonOutputParser()
    chain =final_prompt | llm_instance | parser
    result = chain.invoke({"text": response})
    return result

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
    conversation = ConversationChain(llm=llm_Normal(model_name=model_name), memory=memory)
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
    memory = ConversationBufferMemory(return_messages=True)    
    conversation = ConversationChain(llm=llm_Normal(model_name=model_name), memory=memory)
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
    return full_response

@st.cache_data(show_spinner="Generating the java code...")
def getjavacode(exec_prompt,userstories,model_name,code):   
    memory_code = ConversationBufferMemory(return_messages=True)    
    conversation_chain = ConversationChain(llm=llm_Normal(model_name=model_name), memory=memory_code)
    final_prompt = PromptTemplate.from_template(exec_prompt)
    formatted_prompt = final_prompt.format(user_stories=userstories,PLSQL_CODE=code)  
    response = conversation_chain.predict(input=formatted_prompt)    
    # Initialize the full response
    full_response = response   
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode(full_response)
    st.write("--> Number of tokens:", len(tokens))
    max_tokens = 4000
    needs_continuation = len(tokens) >= max_tokens - 600
    while needs_continuation:
        continuation_prompt = "Please continue where you left off."
        continuation_response = conversation_chain.predict(input=continuation_prompt)
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

@st.cache_data(show_spinner="Generating the java code...")
def getjavacode_new(exec_prompt,userstories,model_name,plsql_str):   
    memory_code = ConversationBufferMemory(return_messages=True)    
    conversation_chain = ConversationChain(
        llm=llm_Normal(model_name=model_name),
          memory=memory_code)
    final_prompt = PromptTemplate.from_template(exec_prompt)    
    full_response =""
    
    for i in range(len(userstories)):        
        formatted_prompt = final_prompt.format(user_stories=userstories[i])
        response = conversation_chain.predict(input=formatted_prompt)
        # Initialize the full response..        
        full_response += " " + response
        print("For Loop -> ",i)
        encoding = tiktoken.encoding_for_model("gpt-4o")
        tokens = encoding.encode(full_response)
        print("--> Number of tokens:", len(tokens))
    with st.expander('memeorycheck'):
        st.write(memory_code.load_memory_variables({}))
    return full_response 
        





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

def get_code(userstories,code,plsql_str):
    result = getjavacode_new(exec_prompt=code_gen,userstories=userstories,model_name="gpt-4o-mini",plsql_str=plsql_str)
    return result

