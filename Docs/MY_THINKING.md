# Personal Codex Agent:

## Prompt Histories
The Personal Codex Agent was designed to answer questions about my skills, experiences, and projects in various tones. Below is an example of how the prompt was crafted and iterated:

Initial Prompt Idea
- Objective: Create an AI agent that responds as me, using my CV, resume, and project files as a knowledge base.
- First Draft (in `Personal_Codex_Agent.py`):
  - Used a simple prompt asking the LLM to "answer as Nkosingiphile Xaba."
  - Issue: Responses were generic and lacked structure.
- Refined Prompt (current version):
  - Added explicit role, task, and guidelines for authenticity, evidence-based answers, and narrative flow.
  - Included mode-specific instructions (e.g., Interview Mode, Poetic Mode).
  - Example: "Answer the question '{input}' in the first person... following this style: {mode_instruction}."

### Challenges and Iterations
- Challenge: Ensuring responses were grounded in documents.
  - Solution: Implemented RAG with Chroma vector store, chunking documents into 1000-char segments for retrieval.
- Challenge: Supporting multiple response tones.
  - Solution: Created a dictionary of mode instructions and dynamically inserted them into the prompt template.
- Challenge: Streamlit UI error with key mismatch.
  - Solution: Fixed `result["result"]` to `result["answer"]` in `Streamlit.py` to match RAG chain output.

## Agent Instructions
The agent follows a structured RAG pipeline:
1. Document Loading: Loads PDFs and text files from `My content/`.
2. Vector Store Setup: Chunks documents and embeds them using `all-MiniLM-L6-v2`.
3. Retrieval and Generation: Retrieves top-2 relevant chunks and generates answers with GPT-4o-mini.

### Sub-Agent Roles
- Document Processor: Handles loading and chunking of PDFs/TXT files (function: `load_documents`).
- Embedding Generator: Converts text chunks to vectors (function: `setup_vector_store`).
- Response Generator: Combines retrieved context with mode-specific prompts to generate answers (function: `setup_rag_chain`).
- UI Manager: Manages user input, chat history, and display in Streamlit (function: `main` in `Streamlit.py`).

## Development Notes
- Why LangChain?: Chosen for its robust RAG framework and integration with Hugging Face embeddings and OpenAI LLMs.
- Why Streamlit?: Simple, Python-based UI for rapid prototyping and deployment.
- Security Note: Hardcoded API key in `Personal_Codex_Agent.py` should be replaced with `os.getenv("OPENAI_API_KEY")` for production.