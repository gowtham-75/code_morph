import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai.chat_models import AzureChatOpenAI
import warnings
import tiktoken

load_dotenv()

AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
DEPLOYMENT_NAME = os.environ['DEPLOYMENT_NAME']
model_name = "gpt-4o"

def llm_Normal(model_name):
    llm = AzureChatOpenAI(azure_deployment=DEPLOYMENT_NAME,  
    api_key=AZURE_OPENAI_API_KEY,          
    azure_endpoint=AZURE_ENDPOINT,  
    api_version="2023-09-01-preview" ,
    temperature=0.5,
    model=model_name,
    max_tokens = 4000
    
    )
    return llm



warnings.filterwarnings('ignore')
_ = load_dotenv()

code_dir_name = "./code1"
 
def initialize_conversation(model_name):
    """
    Initialize the conversation chain with the specified model
    """
    chat = AzureChatOpenAI(
        azure_deployment=os.environ["DEPLOYMENT_NAME"],
        openai_api_version="2024-09-01-preview",
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        temperature=0.5,
        max_tokens=4000,
        model_name=model_name
    )
    memory = ConversationBufferMemory(return_messages=True)
    return ConversationChain(llm=chat, memory=memory)


def llm1(prompt, model_name):
    """
    Handle LLM interactions with automatic continuation for long responses
    """
    # Initialize conversation with the selected model
    conversation = initialize_conversation(model_name)
    
    # Generate the initial response
    response = conversation.predict(input=prompt)
    
    # Initialize the full response
    full_response = response   
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode(full_response)

    st.write("Number of tokens:", len(tokens))
    max_tokens = 4000  
    
    needs_continuation = len(tokens) >= max_tokens - 400
    while needs_continuation:
        continuation_prompt = "Please continue where you left off."
        continuation_response = conversation.predict(input=continuation_prompt)
        full_response += " " + continuation_response
        tokens_continuation = encoding.encode(continuation_response)
        needs_continuation = len(tokens_continuation) >= max_tokens - 400        
        # st.write(continuation_response)

        # Add a safeguard to prevent infinite loops
        if len(full_response) > max_tokens * 7:  # Limit to 7 continuations
            break      
    
    return full_response



def llm(prompt, model_name):
    """
    Handle LLM interactions with automatic continuation for long responses
    """
    # Initialize conversation with the selected model
    conversation = initialize_conversation(model_name)
    
    # Generate the initial response
    response = conversation.predict(input=prompt)
    
    # Initialize the full response
    full_response = response   
    encoding = tiktoken.encoding_for_model("gpt-4o")
    tokens = encoding.encode(full_response)

    st.write("Intial Number of tokens:", len(tokens))
    max_tokens = 4000  
    
    needs_continuation = len(tokens) >= max_tokens - 400
    while "E-N-D" not in response and needs_continuation:
        continuation_prompt = "Please continue where you left off."
        continuation_response = conversation.predict(input=continuation_prompt)
        full_response += " " + continuation_response
        tokens_continuation = encoding.encode(continuation_response)
        needs_continuation = len(tokens_continuation) >= max_tokens - 400  
        response = continuation_response      
        # st.write(continuation_response)
        print(full_response)

        # Add a safeguard to prevent infinite loops
        if len(full_response) > max_tokens * 5:  # Limit to 7 continuations
            break      
    st.write("Final Number of tokens:", len(encoding.encode(full_response)))
    return full_response

