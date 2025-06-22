import streamlit as st
import openai
import os

st.set_page_config(page_title="Classroom AI Chatbot", layout="centered")
st.title("🎓 AI Classroom Chatbot")
st.write("Ask questions about your subjects like C, Java, Python, HTML, etc.")

openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = st.text_input("👨‍🎓 You:", "")

def get_openai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for college students. Answer clearly and helpfully."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Error: {e}"

if user_input:
    with st.spinner("Thinking..."):
        response = get_openai_response(user_input)
        st.markdown(f"**🤖 AI:** {response}")
