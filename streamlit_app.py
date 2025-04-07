import streamlit as st
from modules.chatbox import chatbox
from modules.file_qa import file_qa
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

css_file_path = os.path.join("assets", "styles.css")
with open(css_file_path, encoding="utf-8") as f:
    css = f.read()

st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Chatbot")
    
    option = st.radio("Choose the option:", ("Chatbot", "File Q&A"))

    if st.button("Remove history chat"):
        if "chatbot_messages" in st.session_state:
            st.session_state["chatbot_messages"] = []
        if "file_qa_messages" in st.session_state:
            st.session_state["file_qa_messages"] = []
        st.rerun()

    st.markdown("---")
    st.markdown("**API KEY**")
    api_key = st.text_input("Enter your AI API Token:", type="password", value="sk-xxx")
    st.markdown("[Get API token](https://huggingface.co/settings/tokens)")
    # st.markdown("[View the source code]")
    # st.button("Open in GitHub Codespaces")
    st.link_button("Open in GitHub Codespaces", "https://github.com/trgtanhh04/chatbox-app")

if option == "Chatbot":
    st.title("🔎Chat with search")
    st.markdown('<p class="subtext">A Streamlit chatbot powered by OpenAI 🚀</p>', unsafe_allow_html=True)
    st.markdown('<p class="welcome-message">How can I help you?</p>', unsafe_allow_html=True)
    chatbox()  
elif option == "File Q&A":
    st.title("📝 File Q&A ")
    st.markdown('<p class="subtext">Ask questions about your files.</p>', unsafe_allow_html=True)
    file_qa()  

# remove history chat