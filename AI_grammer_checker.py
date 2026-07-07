import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Grammar Checker", page_icon="✍", layout="wide")

st.title("✍ AI Grammar Checker")
st.write("Correct grammar, improve writing, rewrite professionally, and explain grammar mistakes.")

text = st.text_area(
    "Enter your text",
    height=200,
    placeholder="Type your sentence here..."
)

if st.button("Check Grammar"):

    if text.strip() == "":
        st.warning("Please enter some text.")
    else:

        prompt = f"""
You are an expert English grammar teacher.

Analyze the following text carefully.

Return your answer in the following format.

## Grammar Corrected
(correct sentence)

## Improved Writing
(improved sentence)

## Professional Rewrite
(professional version)

## Grammar Mistakes
- List every mistake.

## Explanation
Explain each grammar mistake clearly.

## Grammar Rules
Mention the grammar rule used.

Text:
{text}
"""

        with st.spinner("Checking..."):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.4
            )

        answer = response.choices[0].message.content

        st.success("Completed!")

        st.markdown(answer)
