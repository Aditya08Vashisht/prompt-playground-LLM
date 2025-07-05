import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


st.set_page_config(page_title="Prompt Playground", page_icon="🧠")
st.title("🧠 Prompt Playground – Zero-Shot vs Few-Shot vs CoT")

# Sidebar options
mode = st.sidebar.selectbox("Choose Prompting Mode", ["Zero-shot", "Few-shot", "Chain-of-Thought"])
model = st.sidebar.selectbox(
    "Choose Model",
    [
        "openai/gpt-3.5-turbo",
        "openai/gpt-4",
        "anthropic/claude-3-haiku",
        "mistralai/mistral-7b-instruct",
        "meta-llama/llama-3-8b-instruct"
    ]
)

# Input Prompt
user_input = st.text_area("Enter your prompt:")

# Few-shot examples
few_shot_examples = """Q: What is the capital of France?\nA: Paris\n\nQ: What is the capital of Germany?\nA: Berlin\n\nQ: """

# CoT example prefix
cot_prefix = """Q: Jane had 3 apples. She bought 2 more. How many apples does she have now?\nA: Let's think step by step.\nJane had 3. She bought 2. Total is 5.\n\nQ: """

# Function to build final prompt
def build_prompt(mode, user_input):
    if mode == "Zero-shot":
        return user_input
    elif mode == "Few-shot":
        return few_shot_examples + user_input
    elif mode == "Chain-of-Thought":
        return cot_prefix + user_input

# When user clicks Submit
if st.button("Submit"):
    final_prompt = build_prompt(mode, user_input)
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": final_prompt}
                ],
                temperature=0.7
            )

            answer = response.choices[0].message.content
            st.success("Done!")
            st.markdown("### 🔍 Prompt Used:")
            st.code(final_prompt)
            st.markdown("### 💬 Model Response:")
            st.markdown(answer)

        except Exception as e:
            if "insufficient_quota" in str(e):
                st.error("⚠️ Insufficient quota. Check your OpenRouter usage or API key.")
            else:
                st.error(f"❌ Error: {e}")
