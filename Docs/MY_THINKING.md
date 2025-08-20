# **Personal Codex Agent**
**Prompt Histories**

The Personal Codex Agent was designed to answer questions about my skills, experiences, and projects in various tones. Below is an example of how the prompt was crafted and iterated:

**Initial Prompt Idea**

**Objective**: Create an AI agent that responds as me, using my CV, transcript, resume, and project files as a knowledge base.

**First Draft (in Personal_Codex_Agent.py):**

Used a simple prompt asking the LLM to "answer as Nkosingiphile Xaba."

Issue: Responses were generic and lacked structure.

**Refined Prompt (current version)**

Added explicit role, task, and guidelines for authenticity, evidence-based answers, and narrative flow.

Included mode-specific instructions (e.g., Interview Mode, Poetic Mode).

The UI can now accept documents that are uploaded to enhance the context.

**Example:**

Answer the question '{input}' in the first person... following this style: {mode_instruction}.

## **Challenges and Iterations**

**Challenge**: Ensuring responses were grounded in documents.

**Solution**: Implemented RAG with a Chroma vector store, chunking documents into 1000-character segments for retrieval.

**Challenge**: Supporting multiple response tones.

**Solution**: Created a dictionary of mode instructions and dynamically inserted them into the prompt template.

**Challenge**: Streamlit UI error with key mismatch.

**Solution**: Fixed result["result"] to result["answer"] in Streamlit.py to match RAG chain output.

**Challenge**: Avoiding hallucinated answers not backed by documents.

**Solution**: If no relevant info is found, the agent responds with:

Not found in the documents.


**Challenge**: Getting the LLM to also use newly uploaded documents on Streamlit Cloud.

**Problem**: At first, the LLM only read from the static repository folder (My content/) and ignored documents uploaded by the user.

**Solution**: Added a Streamlit file uploader that saves uploaded files into the same content directory. These files are then processed through load_documents() and included in the Chroma vector store, so the model uses both repo documents and any new uploads for generating contextually accurate answers.


## **Workflow Diagram**

**A** [User in Streamlit UI] -->|Enters Question + API Key| B[Streamlit Frontend]

**B** -->|Uploads Files (PDF/TXT) + Sends Input| C[Backend: Personal_Codex_Agent]

**C** -->|Loads PDFs + TXT from 'My content/' including uploaded files| D[Document Processor]

**D** -->|Chunks + Embeds| E[Vector Store: ChromaDB]

**E** -->|Retrieves Relevant Chunks| F[LLM + Mode Prompting]

**F** -->|Generates Answer| G[Streamlit UI Output]



## **Agent Instructions**

The agent follows a structured RAG pipeline:

**Document Loading**

Uses the function load_documents() to read files from the My content/ directory.

Supports both PDFs (via PyPDF2.PdfReader) and plain text files.

Extracted text from each file is appended into a list of document strings.

Automatically includes newly uploaded documents from the Streamlit file uploader.

If the directory doesn’t exist, it’s created automatically.

If any file path is invalid, a FileNotFoundError is raised.

**Vector Store Setup**

Documents are chunked and embedded with HuggingFaceEmbeddings (all-MiniLM-L6-v2).

Chunks are stored in a Chroma vector database for fast similarity search.

Function: setup_vector_store().

**Retrieval and Generation**

Retrieves top relevant chunks using similarity_search.

Passes retrieved text into the LLM with mode-specific instructions.

If no relevant context is found, responds with "Not found in the documents."

Function: answer_question().

**API Key Handling**

The user provides their OpenAI API key through the Streamlit UI (st.text_input).

Once entered, the key is set dynamically in os.environ["OPENAI_API_KEY"].

The backend (Personal_Codex_Agent.py) automatically uses this key for all OpenAI API calls.

This ensures security and allows each user to bring their own key.

## **Sub-Agent Roles**

**Document Processor**

Handles loading and chunking of PDFs/TXT files.

Function: load_documents().

Uses PyPDF2 for PDFs and basic text I/O for .txt files.

**Embedding Generator**

Converts text chunks to vectors with HuggingFaceEmbeddings (all-MiniLM-L6-v2).

Function: setup_vector_store().

**Response Generator**

Combines retrieved context with mode-specific prompts to generate answers.

If context is missing, gracefully responds "Not found in the documents."

Function: answer_question().

**UI Manager**

Manages user input, chat history, API key entry, and display in Streamlit.

Handles uploaded documents dynamically.

Function: main() in Streamlit.py.

Development Notes

**Why LangChain?**
Chosen for its robust RAG framework and integration with Hugging Face embeddings + OpenAI LLMs.

**Why Streamlit?**
Simple, Python-based UI for rapid prototyping and deployment.

**Security Note**:
API keys are not hardcoded. Instead, users securely input their key in the Streamlit UI, which is passed to the backend dynamically via environment variables.
