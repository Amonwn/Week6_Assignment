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
#ref from https://www.kaggle.com/code/amirmotefaker/chatgpt-web-application-using-streamlit/comments
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gpt2" 
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids, temperature=0.8)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)


### Display
st.write(
    generated_text.choices[0].message.content
) 

### Request the answer to the prompt2 (predictable)
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = "gpt2" 
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids, temperature=0.2)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)


### Display
st.write(
    generated_text.choices[0].message.content
) 

