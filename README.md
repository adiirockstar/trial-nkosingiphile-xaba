📖 **Personal Codex Agent**
The Personal Codex Agent is an AI-powered assistant built with LangChain, Streamlit, and GPT that answers questions about you based on your CV, academic transcript, motivation letter, projects, and other documents.
It acts like your personal knowledge base:

Reads your documents (PDF, TXT, PY) from the My content/ folder.
Lets you upload new documents via the Streamlit app.
Uses RAG (Retrieval-Augmented Generation) to ground all answers in your real experiences.
Provides multiple response styles (Interview Mode, Humble Brag Mode, Poetic Mode, etc.).
Refuses to hallucinate: if information is missing, it says: "Not found in the documents."

🚀 **Features**

Custom Knowledge Base → Ingests documents from My content/ + uploaded files.
Multi-Tone Responses → Choose how answers should sound:
🎙 Interview Mode → formal & professional
✍️ Personal Storytelling → reflective & narrative
⚡ Fast Facts → concise bullet points
💪 Humble Brag → confident, self-promotional
🎨 Poetic → metaphorical, emotional, and lyrical


Real-Time Uploads → Add new documents without restarting the app.
Dark/Light Themes → Customize UI theme.
Chat UI → Clean, chat-like interface with user & assistant message bubbles.

🛠️ **Installation**

Clone the repository
git clone https://github.com/Nkosingiphile18/personal-codex-agent.git
cd personal-codex-agent


**Create a virtual environment**
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


**Install dependencies**
pip install -r requirements.txt

**Dependencies include:**

streamlit (UI)
langchain, chromadb, langchain-openai, langchain-community, langchain-huggingface
pysqlite3, PyPDF2, dotenv


**Set your API key**
Create a .env file in the repo root:
enter it directly in the Streamlit sidebar at runtime.


▶️ **Running the App**
Start Streamlit:
streamlit run Streamlit.py

This will open the app in your browser at https://personal-codex-agent-j3jlpeqwhrxdynqu8pxftm.streamlit.app/
📂 Project Structure
📦 personal-codex-agent
 ┣ 📂 My content/              # Put your CV, transcript, projects here (PDF/TXT/PY)
 ┣ 📜 Personal_Codex_Agent.py  # Core logic (RAG, vector store, LLM)
 ┣ 📜 Streamlit.py             # Web UI
 ┣ 📜 requirements.txt         # Dependencies
 ┗ 📜 README.md                # Project documentation

💡 **How It Works**

Load documents → Reads PDFs & TXTs from My content/ + any new uploads.
Chunk & Embed → Splits text into chunks, embeds with MiniLM-L6-v2.
Store & Retrieve → Stores in Chroma DB, retrieves relevant chunks per query.
Prompt & Generate → Feeds context into GPT (gpt-4o-mini) with a mode-specific style.
Answer → If grounded in documents → answers; else → "Not found in the documents."

📌 **Example Questions**

"What are your strongest technical skills?" → Interview Mode
"Tell me about a time you solved a complex problem." → Storytelling Mode
"List your programming languages." → Fast Facts Mode
"What achievement are you most proud of?" → Humble Brag Mode
"Describe your career journey as a poem." → Poetic Mode

⚠️ **Notes**

All documents must be placed in My content/ or uploaded in-app.
Only PDF, TXT, and PY files are supported.
The agent does not fabricate answers – it will only answer based on your content.

📜 **License**
MIT License. Free to use and modify.
