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
number = st.number_input("Insert expected number of token to be used", min_value=10, max_value=200)

### Request the answer to the prompt1 (creativity)
"""
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gpt2" 
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids, max_new_tokens=number)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
"""

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
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
    generated_text.choices[0].message.content
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

