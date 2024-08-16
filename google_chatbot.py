'''
A basic AI chatbot based on google ai api.Just created for learning purpose.I know it's weird but I have just put it here for future uses if it will be needed
'''
import os
from dotenv import load_dotenv

load_dotenv()
googleai_api_key=os.getenv('googleai_api_key')

import google.generativeai as genai
import os

genai.configure(api_key=googleai_api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    proompt=input("User: ")
    if proompt=='exit':
        print('\n\n','-'*50)
        print("| Thank you for using Adnan's ultimate AI proompter |")
        print('-'*50,'\n\n')
        break
    response = model.generate_content(proompt)
    print("AI: ",response.text)