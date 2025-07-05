# 🧠 Prompt Playground – Zero-Shot vs Few-Shot vs CoT

This is a beginner-friendly interactive playground built with **Streamlit** to experiment with different prompt engineering strategies for **LLMs (Large Language Models)**.

🔍 Try different modes:
- Zero-shot
- Few-shot
- Chain-of-Thought (CoT)

⚙️ Works with models via [OpenRouter.ai](https://openrouter.ai/) — including:
- `mistralai/mistral-7b-instruct` ✅
- `meta-llama/llama-3-8b-instruct`
- `anthropic/claude-3-haiku`

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/66ab673f-6e17-4a93-8c5c-a75a1e024dc7)


---

## 🛠️ How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/Aditya08Vashisht/prompt-playground-LLM.git
cd prompt-playground-LLM

2. Create and activate a virtual environment:
in terminal-
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

bash-
pip install -r requirements.txt

4. Create a .env file using .env.example:

bash- 
OPENROUTER_API_KEY=your_actual_key_here

5. Run the app:

bash- 
streamlit run app.py
