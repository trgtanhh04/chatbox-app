# pages/chatbox.py
import streamlit as st
from .utils import call_llm, llm_client

def display_chat():
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.markdown(f'<div style="text-align: right; color: #ADD8E6;">**Bạn**: {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; color: #FFFFFF;">**Bot**: {message["content"]}</div>', unsafe_allow_html=True)

def chatbox():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    with st.container():
        prompt = st.text_input("Your message", key="chat_input")

        if st.button("Send message"):
            if prompt:
                response = call_llm(inference_client=llm_client, prompt=prompt)
                
                st.session_state["messages"].append({"role": "user", "content": prompt})
                st.session_state["messages"].append({"role": "bot", "content": response})
                
                display_chat()
            else:
                st.write("Please enter the question.")

