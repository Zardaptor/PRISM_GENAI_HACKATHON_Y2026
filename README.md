# 📱 Samsung PRISM Gen AI Hackathon - Theme 2
## 🛡️ Team Gladiators (Vellore Institute of Technology)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini_3.8_Flash-8E75B2?logo=google&logoColor=white)
![Pydantic](https://img.shields.io/badge/Validation-Pydantic-e92063?logo=pydantic&logoColor=white)

### 🎥 Live Demonstration
👉 [**Click Here to Watch the Demo Video**](https://drive.google.com/file/d/1irloLuqWdeBMdrsZ9h0B1Z-5Kt64n_Ou/view?usp=sharing) 👈

### 📊 Official Presentation
The detailed technical presentation (**\VITV_Gladiators_Submission.pptx\**) is included in the root of this repository.

---

### 🚀 Project Overview (Smart Guided Troubleshooting Engine)
We built an **Agentic LLM pipeline** that transforms unstructured, chaotic technical knowledge (SIIS documents) into highly deterministic, schema-compliant JSON structures. This engine maps customer hardware and software faults directly to actionable, executable device settings (Deep Links) using a custom RAG architecture.

### ✨ Innovation & Brownie Points
1. **Dynamic Local RAG Retriever:** 
   We did not just dump 500+ links into the prompt. We implemented a custom token-overlap algorithm to filter 500+ Deep Links down to the **top 15 highest-confidence candidates** before inference. This drastically reduces token latency and completely eliminates LLM hallucinations.
2. **Real-time Agent Execution Trace:** 
   Built-in backend logging is surfaced directly in the UI, proving the zero-latency RAG routing to judges in real-time.
3. **Samsung One UI Aesthetic:** 
   We abandoned standard Streamlit styling and injected custom CSS to perfectly mirror the native Samsung Dark Mode design language.
4. **Strict Pydantic Validation:** 
   Guarantees 100% adherence to the required \schema.py\ standard.

---

### ⚙️ Setup & Installation

**1. Clone the repository:**
\\ash
git clone https://github.com/Zardaptor/PRISM_GENAI_HACKATHON_Y2026.git
cd PRISM_GENAI_HACKATHON_Y2026
\
**2. Install dependencies:**
\\ash
pip install -r requirements.txt
\
**3. Run the application:**
\\ash
streamlit run app.py
\
**4. Start Troubleshooting:**
Enter your Gemini API Key in the left sidebar (or use the built-in cache) to begin autonomous hardware troubleshooting!
