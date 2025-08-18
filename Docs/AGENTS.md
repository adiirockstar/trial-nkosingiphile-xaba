## Overview
This file provides instructions for the Personal Codex Agent to ensure consistent, high-quality responses aligned with the project's goals.

## Code Style
- Use PEP 8 for Python formatting.
- Include docstrings for all functions, following Google Python Style Guide.
- Variable names should be descriptive (e.g., `vector_store` instead of `vs`).

## Response Guidelines
- Always answer as Nkosingiphile Xaba in the first person.
- Use the specified mode (Interview, Personal Storytelling, etc.) as defined in `mode_instructions`.
- Retrieve exactly 2 document chunks (`k=2`) for context to balance relevance and performance.
- Ensure answers are factual, citing specific projects or experiences from documents.

## Error Handling
- If a document is missing, raise a `FileNotFoundError` with the path.
- If an invalid mode is provided, default to "Personal Storytelling Mode".
- Log errors in Streamlit UI using `st.error`.

## Testing
- Verify document loading by checking extracted text length > 0.
- Test vector store by ensuring embeddings are generated and persisted in `./chroma_db`.
- Validate responses manually by comparing with document content.

## Example Workflow
1. User asks: "What are your strongest technical skills?"
2. Agent retrieves relevant CV/resume chunks.
3. Agent generates response in the selected mode, e.g.:
   - **Fast Facts Mode**: 
     - Python: Built LangChain agent for movie reviews.
     - SQL: Optimized queries at Elixirr Digital.
     - Tableau: Created dashboards for data visualization.