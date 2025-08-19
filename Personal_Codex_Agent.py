__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from dotenv import load_dotenv
import os
import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
import PyPDF2
from pathlib import Path
load_dotenv()
def get_openai_api_key():
    """
    Get the OpenAI API key from environment variables.
    Raises an error if not found.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Please set it in the Streamlit sidebar.")
    return api_key
# Initialize embeddings and LLM
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def load_documents():
    """
    Load and extract text from personal documents (PDFs and TXT files).

    Returns:
        list[str]: List of extracted text contents from each document.

    Raises:
        FileNotFoundError: If any document path does not exist.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # folder where script runs
    content_dir = os.path.join(base_dir, "My content")
    # doc_paths = [
    #     "My content/Nkosingiphile_Xaba_CV.pdf",  
    #     "My content/Nkosingiphile_Xaba_Resume.pdf", 
    #     "My content/Nkosingiphile_Motivation_letter.txt",
    #     "My content/LangChain_Agents.py",
    #     "My content/XBXNKO007_Xaba, Nkosingiphile Bayanda.pdf"
    # ]
    
    docs = []
    for filename in os.listdir(content_dir):
        path = os.path.join(content_dir, filename)

        if filename.endswith(".pdf"):
            with open(path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = "".join(page.extract_text() or "" for page in pdf_reader.pages)
                docs.append(text)
        else:
            with open(path, "r", encoding="utf-8") as file:
                docs.append(file.read())
    
    return docs


def setup_vector_store(docs):
    """
    Create and populate a Chroma vector store from document texts.

    Args:
        docs (list[str]): List of document texts to chunk and embed.

    Returns:
        Chroma: Initialized vector store persisted to ./chroma_db.
    """
    try:
        client = chromadb.Client()  # In-memory client for Streamlit Cloud
        documents = load_documents()
        if not documents:
            print("Error: No documents available for vector store.")
            return None
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text("\n".join(documents))
        vector_store = Chroma.from_texts(
            texts=chunks,
            embedding=embeddings,
            collection_name="personal_codex",
            client=client
        )
        return vector_store
    except Exception as e:
        print(f"Chroma setup failed: {e}")
        return None

def setup_rag_chain(vector_store, mode):
    """
    Set up the RAG chain with a custom prompt template based on the selected mode.

    Args:
        vector_store (Chroma): The vector store for retrieval.
        mode (str): Response mode (e.g., "Interview Mode").

    Returns:
        tuple: (RetrievalChain, str) - The RAG chain and mode instruction.
    """
    mode_instructions = {
        "Interview Mode": "Answer in a professional, formal tone suitable for a job interview, focusing on clarity and relevance to my qualifications.",
        "Personal Storytelling Mode": "Answer in a reflective, narrative style, sharing personal insights and experiences as if telling a story.",
        "Fast Facts Mode": "Answer in a concise, bullet-point or TL;DR format, summarizing key points efficiently. Begin with the skill/strength name followed by a proficiency level (if relevant) in bold.",
        "Humble Brag Mode": "Answer with confidence and enthusiasm, highlighting my achievements with a self-promotional tone while staying truthful.",
        "Poetic Mode": "Answer in Metaphors, similes, and vivid imagery to paint ideas as pictures. Use alliteration, rhythm, and flow to create musicality in the language. Use emotion-driven language that stirs feeling, even for abstract topics. Keep it short."
    }

    mode_instruction = mode_instructions.get(mode, mode_instructions["Personal Storytelling Mode"])
    prompt_template = PromptTemplate(
        input_variables=["input", "context", "mode_instruction"],
        template="""
Role & Identity:
You are Nkosingiphile Xaba, a recent BSc Applied Statistics graduate from the University of Cape Town, 
with demonstrated expertise in Statistics, Python, Java, Tableau, SQL, Mathematics, LangChain, and AI development.
You interned at Elixirr Digital and worked on various projects, including a LangChain agent for movie review analysis.

Task:
Answer the question "{input}" in the first person, as if you are personally speaking and reflecting, following this style: {mode_instruction}.

Knowledge Base:
Use the provided reference materials — {context} — which may include your CV, academic transcript,
motivation letter, project portfolio, code snippets, and other personal documents.
Treat these as your authoritative memory. Before answering, analyze and retrieve the most relevant details
to ensure your answer is specific, factually accurate, and grounded in your real experiences.

Response Guidelines:
1. Authenticity & Reflection – Speak in a personal, genuine tone that reflects your real motivations, values, and thought process.
2. Evidence-Based – Support your answer with concrete examples, project descriptions, or measurable results.
3. Narrative Flow – Where possible, tell a brief story about how you acquired a skill, overcame a challenge, or applied knowledge in a real project.
4. Context Linking – Explicitly link your skills and experiences to the question.
5. Clarity & Professionalism – Keep your response well-structured, engaging, and concise.
6. Opening Style – Begin your answer immediately with a personal statement, reflection, or example relevant to the question. Avoid generic introductions such as “In a professional context” or “When I reflect on…”.

Reasoning Process (Internal):
- Identify the key themes of the question.
- Scan {context} for relevant experiences or achievements.
- Organize answer: context → action → result → reflection.
- Ensure factual alignment with documents before finalizing.
"""
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    api_key = get_openai_api_key()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9, api_key=api_key)
    
    stuff_chain = create_stuff_documents_chain(llm, prompt_template)

    return create_retrieval_chain(retriever, stuff_chain), mode_instruction

def answer_question(question, mode="Personal Storytelling Mode"):
    """
    Generate an answer to a question using the RAG chain.

    Args:
        question (str): The user's question.
        mode (str, optional): Response mode. Defaults to "Personal Storytelling Mode".

    Returns:
        str: The generated answer from the LLM.
    """
    docs = load_documents()
    vector_store = setup_vector_store(docs)

    qa_chain, mode_instruction = setup_rag_chain(vector_store, mode)

    # Only pass variables expected by the prompt + retriever
    result = qa_chain.invoke({"input": question, "mode_instruction": mode_instruction})
    return result["answer"]
