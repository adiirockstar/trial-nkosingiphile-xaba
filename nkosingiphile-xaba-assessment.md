# Candidate Evaluation: Nkosingiphile Xaba

**Repository:** [Nkosingiphile18/personal-codex-agent](https://github.com/Nkosingiphile18/personal-codex-agent)

## Rubric Evaluation

| Category | Score (0–5) | Notes |
| --- | --- | --- |
| Context Handling | **4** | RAG chain retrieves from personal docs and falls back to "Not found" when context missing [`Personal_Codex_Agent.py` lines 140-142](Personal_Codex_Agent.py#L140-L142).
| Agentic Thinking | **3** | Five tone modes and theming show personality but limited behavioral nuance [`Personal_Codex_Agent.py` lines 100-108](Personal_Codex_Agent.py#L100-L108); [`Streamlit.py` lines 111-120](Streamlit.py#L111-L120).
| Use of Personal Data | **4** | CV, resume, transcript, and motivation letter loaded from `My content/` directory (`My content`).
| Build Quality | **2** | Unused parameters, redundant vector store rebuilds, heavy dependencies, and no tests [`Personal_Codex_Agent.py` lines 60-75](Personal_Codex_Agent.py#L60-L75); [`Personal_Codex_Agent.py` lines 165-167](Personal_Codex_Agent.py#L165-L167); [`requirements.txt` lines 12-16](requirements.txt#L12-L16).
| Voice & Reflection | **3** | Prompt enforces first-person reflective tone [`Personal_Codex_Agent.py` lines 112-132](Personal_Codex_Agent.py#L112-L132).
| Bonus Effort | **3** | Extra modes (e.g., Poetic) and dark theme add polish [`Personal_Codex_Agent.py` line 105](Personal_Codex_Agent.py#L105); [`Streamlit.py` lines 118-144](Streamlit.py#L118-L144).
| AI Build Artifacts | **3** | `Docs/MY_THINKING.md` documents prompt iterations and design decisions.
| RAG Usage (Optional) | **4** | Effective Chroma-based retrieval and mode-aware prompt assembly [`Personal_Codex_Agent.py` lines 146-152](Personal_Codex_Agent.py#L146-L152).
| Submission Completeness | **4** | GitHub repo, deployed app, and walkthrough video provided in email.

**Total Score:** **30 / 45**

## Critical Feedback & Suggestions

1. **Unused `docs` parameter in `setup_vector_store`**  
   The function accepts a `docs` argument but reloads documents internally, making the parameter redundant and confusing [`Personal_Codex_Agent.py` lines 60-75](Personal_Codex_Agent.py#L60-L75).

2. **Vector store rebuilt on every question**  
   `answer_question` reloads documents and recreates the vector store for each query, increasing latency and cost [`Personal_Codex_Agent.py` lines 165-167](Personal_Codex_Agent.py#L165-L167). Persist the store or cache it after initial creation.

3. **Heavy, unnecessary dependencies**  
   `requirements.txt` includes `torch`, `torchvision`, and `torchaudio`, which are unused and significantly inflate install size [`requirements.txt` lines 12-16](requirements.txt#L12-L16). Remove unused packages and document remaining ones.

4. **No automated tests**  
   Repository lacks any test files or structure, so behavior is unverified. Introduce a basic `pytest` suite covering document loading and RAG flow.

5. **Potential API key exposure**  
   API key is written directly to `os.environ`, risking leakage in shared deployments [`Streamlit.py` lines 93-104](Streamlit.py#L93-L104). Use `st.secrets` or session state instead.

## Additional Observations

- `Docs/MY_THINKING.md` thoughtfully logs interactions with AI coding agents, showing an AI-native workflow.
- README explains setup and usage but could benefit from clearer formatting and sample commands.

## Testing

- No automated tests are included in the repository.

