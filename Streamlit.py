import streamlit as st
from Personal_Codex_Agent import answer_question

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for ChatGPT-like styling
st.markdown(
    """
    <style>
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
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for settings
with st.sidebar:
    st.title("Personal Codex Settings")
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
            </style>
            """,
            unsafe_allow_html=True
        )

# Main chat interface
st.title("Personal Codex Agent")
st.write("Ask questions about me as a candidate, and I'll answer based on my documents.")

# Display chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input form at the bottom
with st.form(key="input_form", clear_on_submit=True):
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    question_input = st.text_input("Enter a question (e.g., 'What are your strongest technical skills?'):", key="question")
    submit_button = st.form_submit_button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

# Process input and display results
if submit_button and question_input:
    try:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": question_input})
        
        # Get response from backend, passing the tone
        result = answer_question(question_input, mode=tone)
        # Extract the answer string from the dictionary
        answer = result["result"] if isinstance(result, dict) and "result" in result else str(result)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # Rerun to display new messages
        st.rerun()
    except Exception as e:
        st.error(f"Error processing question: {str(e)}")