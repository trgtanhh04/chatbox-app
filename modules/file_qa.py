# pages/file_qa.py
import streamlit as st
from .utils import call_llm, llm_client, read_text_file, read_pdf_file, read_docx_file

def display_chat():
    for message in st.session_state["messages"]:
        if message["role"] == "user":
            st.markdown(f'<div style="text-align: right; color: #ADD8E6;">**Bạn**: {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: left; color: #FFFFFF;">**Bot**: {message["content"]}</div>', unsafe_allow_html=True)

def file_qa():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    uploaded_file = st.file_uploader("Chọn file .txt, .pdf hoặc .docx", type=["txt", "pdf", "docx"])

    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            file_content = read_text_file(uploaded_file)
        elif uploaded_file.type == "application/pdf":
            file_content = read_pdf_file(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            file_content = read_docx_file(uploaded_file)
        else:
            st.error("Định dạng file không được hỗ trợ!")
            file_content = ""
        
        st.write("Nội dung của file:")
        st.write(file_content[:1000])  
        prompt = st.text_input("Nhập câu hỏi của bạn:", key="file_input")

        if st.button("Gửi câu hỏi từ file"):
            if prompt:
                full_prompt = f"Đây là nội dung của tài liệu bạn tải lên:\n{file_content}\nCâu hỏi: {prompt}"
                response = call_llm(inference_client=llm_client, prompt=full_prompt)
                
                st.session_state["messages"].append({"role": "user", "content": prompt})
                st.session_state["messages"].append({"role": "bot", "content": response})
                
                display_chat()
            else:
                st.write("Vui lòng nhập câu hỏi để nhận câu trả lời.")