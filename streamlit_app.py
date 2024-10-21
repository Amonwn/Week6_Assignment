import streamlit as st
from openai import OpenAI
import os

st.title("🎈 My new app")
st.write(
    "What can I help you today?"
)

### Load your API Key
my_secret_key = st.secrets['MyOpenAIKey']
os.environ["OPENAI_API_KEY"] = my_secret_key

prompt = st.text_input("What can I help you today?", " ")

### Request the answer to the promt
client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "Complete the following prefix"},
    {"role": "user", "content": prompt}
  ],
  n=10,
  max_tokens=20
)

### Display
st.write(
    response.choices[0].message.content
) 
