# PRISM_GENAI_HACKATHON_Y2026

## Team: Gladiators
**Theme 2: Smart Guided Troubleshooting Engine**

### 🎥 Demo Video
[**Click Here to Watch the Demo Video**](https://drive.google.com/file/d/1irloLuqWdeBMdrsZ9h0B1Z-5Kt64n_Ou/view?usp=sharing)

### 📊 Presentation
The official submission presentation (\VIT_Theme2_Submission_FINAL.pptx\) is included in the root of this repository.

---

### Project Overview
We built an Agentic LLM pipeline that transforms unstructured technical knowledge (SIIS) into deterministic, schema-compliant JSON structures, mapping hardware faults directly to executable device settings (Deep Links).

### Innovation & Brownie Points
*   **Dynamic Local RAG Retriever:** Implemented a custom keyword-overlap algorithm to filter 500+ Deep Links down to the top 15 candidates before inference, drastically reducing latency and token costs while eliminating LLM hallucination.
*   **Agent Execution Trace:** Built-in backend logging visibility for real-time validation tracking.
*   **Samsung One UI Aesthetic:** Fully customized Streamlit frontend mirroring Samsung's native Dark Mode design language.
*   **Strict Pydantic Validation:** Guarantees 100% adherence to \schema.py\.

### Setup & Installation
1. Install dependencies:
   \\ash
   pip install -r requirements.txt
   \2. Run the application:
   \\ash
   streamlit run app.py
   \3. Enter your Gemini API Key in the sidebar to begin autonomous troubleshooting.
