import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
# from jinja2.compiler import generate

load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Configure Gemini model
model = genai.GenerativeModel('gemini-pro')

st.title('Artificial Intelligence Code Generation')

# Input box
prompt = st.text_area("Enter your code specification", height=100)

if st.button('Generate Code'):
    if prompt:
        try:
            # Construct a more specific prompt, incorporating the user's input
            specific_prompt = f"Generate Python code to {prompt}"

            # Generate code based on the specific prompt
            response = model.generate_content(specific_prompt)
            generated_code = response.text
            st.code(generated_code, language='python')  # Display code with syntax highlighting
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt to generate code.")