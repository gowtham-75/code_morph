import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai.chat_models import AzureChatOpenAI

load_dotenv()
AZURE_OPENAI_API_KEY = os.environ["AZURE_OPENAI_API_KEY"]
AZURE_ENDPOINT = os.environ['AZURE_OPENAI_ENDPOINT']
DEPLOYMENT_NAME = os.environ['DEPLOYMENT_NAME']



def llm(model_name):
    llm = AzureChatOpenAI(azure_deployment=DEPLOYMENT_NAME,  
    api_key=AZURE_OPENAI_API_KEY,          
    azure_endpoint=AZURE_ENDPOINT,  
    api_version="2023-09-01-preview" ,
    temperature=0.1,
    model=model_name,
    max_tokens = 4000
    
    )
    return llm