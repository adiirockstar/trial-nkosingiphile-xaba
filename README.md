# Personal Codex Agent

## Overview
The Personal Codex Agent is a Retrieval-Augmented Generation (RAG) application built with LangChain, Hugging Face embeddings, and OpenAI's GPT-4o-mini model. It serves as a personal AI agent that answers questions about Nkosingiphile Xaba (the developer) based on a knowledge base of personal documents, such as CVs, resumes, motivation letters, academic transcripts, and code snippets.

The agent supports multiple response modes (e.g., Interview, Personal Storytelling, Fast Facts Poetic) to tailor answers in different styles. It uses a vector store (Chroma) for efficient retrieval of relevant document chunks.

The project includes:
- **Personal_Codex_Agent.py**: Core backend logic for loading documents, setting up the vector store, and generating responses via a RAG chain.
- **Streamlit.py**: Frontend Streamlit app providing a chat-like interface for user interactions, with customizable tones and themes.

This tool is ideal for job interviews, personal reflections, or showcasing skills in a dynamic way.

## Features
- **Document Loading**: Supports PDF and text files containing personal info.
- **Vector Embeddings**: Uses `all-MiniLM-L6-v2` for semantic search.
- **RAG Chain**: Combines retrieval with LLM generation for grounded, personalized answers.
- **Modes**: 5 response styles (Interview, Personal Storytelling, Fast Facts, Humble Brag, Poetic).
- **UI**: ChatGPT-like interface with light/dark themes and chat history persistence.
- **Environment**: Requires OpenAI API key (hardcoded in the code; recommended to use environment variables for security).

## Installation
1. **Clone the Repository**: