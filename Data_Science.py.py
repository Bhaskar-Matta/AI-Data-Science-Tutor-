import streamlit as st
import json
import pandas as pd
import google.generativeai as genai
import os
import time
import datetime
import plotly.express as px
import sqlite3
from dotenv import load_dotenv
from fpdf import FPDF
import io
import sys
import pickle
from langchain.schema.runnable import RunnableLambda

# ✅ Securely Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("⚠️ Google GenAI API key is missing! Add it to `.env`.")
    st.stop()

genai.configure(api_key=API_KEY)
MODEL = "gemini-1.5-pro"

SYSTEM_PROMPT = """
You are an helpful DATA SCIENCE AI tutor. Provide answers based on the questions in a structured format.And make answers as simple as you can.
and also if the user askes to stop the response, then stop the response.and if the user askes irrelevant questions, then provide a warning message and politely say to the user iam an data science ai tutor please ask me data science related content.
"""

def get_ai_response(user_input, stop_signal):
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(f"{SYSTEM_PROMPT}\n\nQuestion: {user_input}")
        return response.text if response and response.text else "⚠️ No response generated."
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# ✅ LangChain Runnable for Chat History Storage
def save_chat_history(_input=None):
    with open("chat_history.json", "w") as f:
        json.dump(st.session_state.chat_history, f, indent=4)

def load_chat_history():
    try:
        with open("chat_history.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

save_chat_runnable = RunnableLambda(save_chat_history)

st.set_page_config(page_title="🤖 AI Data Science Tutor", page_icon="🧠", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_chat_history()
if "stop_response" not in st.session_state:
    st.session_state.stop_response = False
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

if not st.session_state.logged_in:
    st.title("🔑 Login to AI Data Science Tutor")
    username = st.text_input("👤 Enter your username:")
    role = st.selectbox("📌 Select Role:", ["User", "Admin", "Business Analyst", "Data Scientist"])
    
    if st.button("🚀 Login"):
        if not username:
            st.warning("⚠️ Please enter your username to proceed.")
        else:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = role
            st.session_state.chat_history = []  # Clear chat history on new login
            st.session_state.last_response = ""
            st.rerun()
    st.stop()

st.sidebar.title("👥 User")
st.sidebar.write(f"👋 Welcome, {st.session_state.username}! ({st.session_state.role})")

st.title("🧠 AI Data Science Tutor")
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.chat_input("💬 Ask an AI-powered question...")
with col2:
    stop_button = st.button("⏹ Stop Response")

if stop_button:
    st.session_state.stop_response = True

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_text = ""
        
        ai_response = get_ai_response(user_input, st.session_state.stop_response)
        for word in ai_response.split():
            if st.session_state.stop_response:
                break
            response_text += word + " "
            time.sleep(0.02)
            response_placeholder.markdown(f"<p style='font-size:14px; line-height:1.5;'>{response_text}</p>", unsafe_allow_html=True)
        
        st.session_state.stop_response = False
        st.session_state.last_response = response_text
    
    st.session_state.chat_history.append(("assistant", response_text))
    save_chat_runnable.invoke(None)

# ✅ Display Chat History
st.subheader("📜 Chat History")
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(f"<p style='font-size:14px; line-height:1.5;'>{msg}</p>", unsafe_allow_html=True)

# ✅ Code Debugging Feature
st.sidebar.title("🐍 Code Debugger")
code_input = st.sidebar.text_area("✍️ Paste your Python code for debugging")
if st.sidebar.button("🔍 Debug Code"):
    debug_response = get_ai_response(code_input, False)
    st.sidebar.markdown(debug_response)

# ✅ ML Model Evaluation
st.sidebar.title("🤖 ML Model Evaluator")
model_file = st.sidebar.file_uploader("📂 Upload a Pickle (pkl) file of your ML model", type=["pkl"])
if model_file:
    model = pickle.load(model_file)
    eval_response = get_ai_response("Evaluate this ML model.", False)
    st.sidebar.markdown(eval_response)

# ✅ AI-Powered Chat Export to PDF
def export_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "📜 Chat History", ln=True, align="C")
    pdf.ln(5)
    for role, msg in st.session_state.chat_history:
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(0, 8, f"{role.capitalize()}:", ln=True)
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 7, msg)
        pdf.ln(3)
    pdf.output("chat_history.pdf")
    return "chat_history.pdf"

if st.sidebar.button("📥 Export Chat as PDF"):
    pdf_path = export_pdf()
    with open(pdf_path, "rb") as f:
        st.sidebar.download_button(label="⬇️ Download PDF", data=f, file_name="chat_history.pdf", mime="application/pdf")







