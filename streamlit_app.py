import streamlit as st
from openai import OpenAI
import os

st.title("🎈 My new app")
st.write(
    "Let's chat!"
)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

prompt = st.text_input("What can I help you today?", " ")
number = st.number_input("Insert expected number of token to be used", min_value=1)

### Request the answer to the prompt1 (creativity)
#from transformers import pipeline
#generator = pipeline('text-generation', model='gpt2')
#generator("Hello, I'm a language model,", max_length=number, temperature=0.8)

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-2",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  #n=10,
  max_tokens=number,
    temperature=0.8
)

### Display
st.write(
    generator.choices[0].message.content
) 

### Request the answer to the prompt2 (predictable)
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  #n=10,
  max_tokens=number,
    temperature=0.2
)

### Display
st.write(
    response.choices[0].message.content
) 


"""
### Request the answer to the prompt2 (predictable)
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  #n=10,
  max_tokens=number,
    temperature=0.2
)
"""
