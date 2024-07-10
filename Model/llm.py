# from langchain_community.chat_models import ChatOllama

# model = ChatOllama(model="llama3")

# class LanguageModel:
#     def __init__(self):
#         self.model = ChatOllama(
#             model="llama3"
#         )
        
#     def get_response(self, prompt):
#         response = model.invoke(prompt)
#         return response.content

import os
from dotenv import load_dotenv
# import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

Api_key = os.getenv('GOOGLE_API_KEY')

class LanguageModel:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=Api_key
        )
        
    def get_response(self, prompt):
        response = self.model.invoke(prompt)
        return response.content