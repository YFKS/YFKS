"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
import textwrap

from google.ai.generativelanguage_v1 import GenerateContentResponse, SafetySetting
import os
import google.generativeai as genai
import json
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

class YFKS:
    def __init__(self):
        self.messages = []
        with open("python/config/prompt.json", "r", encoding='utf-8') as files:
            self.prompt_json = json.load(files)

        with open("python/config/token.json", "r", encoding='utf-8') as files:
            self.token = json.load(files)
        genai.configure(api_key=self.token['token'])

        # Create the model

        self.model = genai.GenerativeModel(
          model_name="gemini-1.5-pro-exp-0801",
          generation_config= self.prompt_json['config'],
          # safety_settings = Adjust safety settings
          # See https://ai.google.dev/gemini-api/docs/safety-settings
        )
        self.chat_session = self.new_chat()

    def new_chat(self):
        self.messages = self.prompt_json['history']
        return self.model.start_chat(history= self.prompt_json['history'])

    def send_chat(self, mes: str)-> GenerateContentResponse:

        self.messages.append({'role':'user',
                 'parts':[mes]})

        res = self.model.generate_content(self.messages, safety_settings={
            'HARASSMENT':'block_none',
            'HATE_SPEECH':'block_none',
        'SEXUALLY_EXPLICIT': 'block_none'})



#        print(f"YFKS:{res.text}")
        self.messages.append({'role':'model',
                 'parts':[res.text]})
        print("--------------------------------------------------------------")

        return res
