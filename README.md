# **Personal Codex Agent**
**Overview**
The Personal Codex Agent is a Streamlit-based application that allows users to interact with a Retrieval-Augmented Generation (RAG) system. It answers questions about Nkosingiphile Xaba, a BSc Applied Statistics graduate from the University of Cape Town, by leveraging a collection of personal documents (PDFs, TXT files) stored in a Chroma vector database. The system uses LangChain, HuggingFace embeddings, and OpenAI's GPT-4o-mini model to provide contextually relevant and personalized responses in various tones, such as Interview Mode, Personal Storytelling Mode, and more.

## **Features**

**Document Upload**: Upload PDF, TXT, or PY files to the "My content" directory for processing.
**Response Modes**: Choose from multiple response tones:
**Interview Mode**: Professional and formal, ideal for job interviews.
**Personal Storytelling Mode**: Reflective and narrative-driven.
**Fast Facts Mode**: Concise, bullet-point summaries.
**Humble Brag Mode**: Confident and self-promotional.
**Poetic Mod**e: Vivid, metaphorical, and emotion-driven responses.


**Theming**: Switch between Light and Dark themes for the Streamlit interface.
**Chat Interface**: Interactive chat system to ask questions and receive answers based on document content.
**Vector Store**: Uses Chroma to store and retrieve document embeddings for efficient question answering.

## **Prerequisites**

Python 3.8+
OpenAI API key (set in a .env file or via Streamlit sidebar)
Required Python packages (listed in requirements.txt)

**Installation**

Clone the repository:git clone https://github.com/Nkosingiphile18/personal-codex-agent
cd personal-codex-agent


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


**Install dependencies**:pip install -r requirements.txt


Set up the .env file with your OpenAI API key:echo "OPENAI_API_KEY=your-api-key" > .env


Create a directory named My content in the project root to store your documents (PDFs, TXT files, etc.).

**Usage**

Run the Streamlit app:streamlit run Streamlit.py


Open the provided URL in your browser (typically https://personal-codex-agent-j3jlpeqwhrxdynqu8pxftm.streamlit.app/).
In the sidebar:
Enter your OpenAI API key.
Upload documents (PDF, TXT, or PY files) to the "My content" directory.
Select a response tone and theme.


Ask a question in the chat interface, e.g., "What are your strongest technical skills?"
The system will process the question using the RAG pipeline and respond based on the documents and selected tone.\n
eg. The Response I got was(Interview mode):
     "I consider my strongest technical skills to be in Statistics, Python, SQL, and AI development, particularly with frameworks like LangChain. My education in BSc Applied Statistics from the University of Cape Town has equipped me with a robust statistical foundation, which I have effectively applied in both academic and practical contexts.
For instance, during my internship at Elixirr Digital, I developed a LangChain agent for movie review analysis. This project not only honed my programming skills in Python but also deepened my understanding of natural language processing. I faced challenges in ensuring the accuracy and relevance of sentiment analysis, which required meticulous attention to detail and iterative problem-solving. The successful deployment of this agent contributed to improved data insights for the team, illustrating my ability to leverage technical skills to facilitate impactful solutions.

Furthermore, my proficiency in SQL allows me to manipulate and analyze large datasets efficiently. I often utilize Tableau for data visualization, which complements my analytical capabilities and enables me to present complex information in a clear, engaging manner.

Overall, my technical skill set is reinforced by my soft skills—critical thinking, time management, and adaptability—which enable me to navigate complexities and drive innovation effectively, as evidenced by my project successes and academic achievements."

## **Project Structure**

Personal_Codex_Agent.py: Core logic for loading documents, setting up the Chroma vector store, and creating the RAG chain for question answering.
Streamlit.py: Streamlit frontend for user interaction, including file uploads, chat interface, and theme customization.
My content/: Directory to store user-uploaded documents (created automatically if it doesn't exist).
.env: Environment file for storing the OpenAI API key.

**Dependencies**
Key dependencies include:

**streamlit**: For the web interface.
**langchain**: For building the RAG pipeline.
**langchain-huggingface**: For embeddings using the all-MiniLM-L6-v2 model.
**langchain-openai**: For interacting with OpenAI's GPT-4o-mini model.
**chromadb**: For the vector database.
**PyPDF2**: For extracting text from PDF files.
**python-dotenv**: For loading environment variables.

Install all dependencies using:
pip install streamlit langchain langchain-huggingface langchain-openai chromadb PyPDF2 python-dotenv

**Notes**

Ensure documents are placed in the My content directory before running the app, or upload them via the Streamlit interface.
The application requires a valid OpenAI API key to function.
If no documents are found or an error occurs during vector store setup, the system will display an error message.
The Chroma vector store is in-memory for compatibility with Streamlit Cloud.

## **Limitations**

Only supports PDF, TXT, and PY files for document processing.
Requires an active internet connection for OpenAI API calls.
Response quality depends on the content and quality of uploaded documents.

## **Future Improvements**

Add support for additional document formats (e.g., DOCX, MD).
Implement persistent storage for the Chroma vector store.
Enhance error handling for document processing.
Add more response modes or customization options for the prompt template.

**License**
This project is licensed under the MIT License.
