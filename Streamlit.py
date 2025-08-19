import os
import streamlit as st
from Personal_Codex_Agent import answer_question

def save_uploaded_file(uploaded_file):
    """Save uploaded file into 'My content/' directory."""
    content_dir = "My content"
    os.makedirs(content_dir, exist_ok=True)
    file_path = os.path.join(content_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def main():
    """
    Main function to run the Streamlit app for the Personal Codex Agent.
    """
    st.set_page_config(layout="centered")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.markdown(
        """
        <style>
        /* Chat container styling */
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        .user-message {
            background-color: #007bff;
            color: white;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 10px 0;
            max-width: 70%;
            margin-left: auto;
            text-align: right;
        }
        .assistant-message {
            background-color: #e9ecef;
            color: black;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 10px 0;
            max-width: 70%;
            margin-right: auto;
        }
        .input-container {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: white;
            padding: 10px;
            border-top: 1px solid #ddd;
        }
        .stTextInput > div > div > input {
            border-radius: 20px;
            padding: 10px;
        }
        /* Circular image container */
        .circular-image {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto;
            border: 2px solid #333;
            background-color: #000000;
            position: relative;
            color: white;
            text-align: center;
            font-size: 16px;
        }
        .circular-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .upload-text {
            position: absolute;
            z-index: 1;
        }
        /* Rectangular bio container */
        .bio-container {
            background-color: #000000;
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
            max-width: 500px;
            margin-left: auto;
            margin-right: auto;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.title("Personal Codex Settings")
        st.subheader("Upload a new document")
        uploaded_doc = st.file_uploader("Upload PDF, TXT, or PY file", type=["pdf", "txt", "py"], key="doc_uploader")
        if uploaded_doc:
            path = save_uploaded_file(uploaded_doc)
            st.success(f"File saved: {uploaded_doc.name}")
            
        tone = st.selectbox("Response Tone", [
            "Interview Mode",
            "Personal Storytelling Mode",
            "Fast Facts Mode",
            "Humble Brag Mode",
            "Poetic Mode"
        ])
        theme = st.selectbox("Theme", ["Light", "Dark"])
        if theme == "Dark":
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #1e1e1e;
                    color: white;
                }
                .user-message {
                    background-color: #0057b7;
                }
                .assistant-message {
                    background-color: #333;
                }
                .input-container {
                    background: #2a2a2a;
                    border-top: 1px solid #444;
                }
                .bio-container {
                    background-color: #000000;
                    border-color: #555;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

    uploaded_image = st.file_uploader("Upload your picture", type=["jpg", "png", "jpeg"], key="image_uploader")
    if uploaded_image is not None:
        st.markdown(
            f'<div class="circular-image"><img src="data:image/jpeg;base64,{st.image(uploaded_image, output_format="JPEG", use_column_width=False, width=200)._get_base64()}"></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="circular-image"><span class="upload-text">Upload your picture</span></div>',
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="bio-container">
            <h3>About Me</h3>
            <p>Nkosingiphile Xaba, BSc Applied Statistics graduate from UCT</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title("Personal Codex Agent")
    st.write("Ask questions about me as a candidate, and I'll answer based on my documents.")

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.form(key="input_form", clear_on_submit=True):
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        question_input = st.text_input("Enter a question (e.g., 'What are your strongest technical skills?'):", key="question")
        submit_button = st.form_submit_button("Send")
        st.markdown('</div>', unsafe_allow_html=True)

    if submit_button and question_input:
        try:
            st.session_state.messages.append({"role": "user", "content": question_input})
            result = answer_question(question_input, mode=tone)
            answer = result if isinstance(result, str) else result.get("answer", str(result))
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()
        except Exception as e:
            st.error(f"Error processing your question: {e}")

if __name__ == "__main__":
    main()
