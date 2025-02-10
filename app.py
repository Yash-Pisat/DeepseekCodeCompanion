import streamlit as st
import io
import sys
import json
import uuid
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# Custom CSS for styling
theme_css = """
<style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    .sidebar .sidebar-content { background-color: #2d2d2d; }
    .stTextInput textarea { color: #ffffff !important; }
    .stSelectbox div[data-baseweb="select"] { color: white !important; background-color: #3d3d3d !important; }
    .stSelectbox svg { fill: white !important; }
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox("Choose Model", ["deepseek-r1:1.5b", "deepseek-coder:latest "], index=0)
    persona = st.selectbox("Choose AI Persona", ["Beginner Guide 📖", "Debugger 🐞", "Optimized Coder ⚡"], index=0)
    enable_execution = st.checkbox("Enable Python Execution", value=False) if persona in ["Debugger 🐞", "Optimized Coder ⚡"] else False
    st.divider()
    st.markdown("### Model Capabilities")
    st.markdown("""
    - 🐍 Python Expert
    - 🐞 Debugging Assistant
    - 📝 Code Documentation
    - 💡 Solution Design
    """)
    st.divider()
    st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# Define AI behavior based on persona
persona_prompts = {
    "Debugger 🐞": "You are an AI debugging expert. Help users find and fix errors efficiently.",
    "Optimized Coder ⚡": "You are an AI coding expert. Provide the most optimized and efficient solutions.",
    "Beginner Guide 📖": "You are a friendly AI coding assistant for beginners. Explain concepts simply."
}

# Initialize chat engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(persona_prompts[persona])

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]
if "code_history" not in st.session_state:
    st.session_state.code_history = []

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Code Execution Feature (Only for Debugger & Optimized Coder if enabled)
if enable_execution:
    def execute_python_code(code):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(code, {"__builtins__": {"print": print}})
            output = sys.stdout.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = stdout
        return output

    st.subheader("🔹 Code Execution")
    user_code = st.text_area("Enter Python code to execute:")
    if st.button("Run Code"):
        st.write("### Output:")
        output = execute_python_code(user_code)
        st.code(output)
        st.session_state.code_history.append(user_code)  # Store executed code in history

# Chat Input
def generate_ai_response(prompt_chain):
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    if st.session_state.code_history:
        code_history_text = "\n\n".join(st.session_state.code_history)
        prompt_sequence.append(HumanMessagePromptTemplate.from_template(f"Here is the executed Python code history:\n{code_history_text}"))
    return ChatPromptTemplate.from_messages(prompt_sequence)

user_query = st.chat_input("Type your coding question here...")
if user_query:
    st.session_state.message_log.append({"role": "user", "content": user_query})
    with st.spinner("🧠 Processing..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)
    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()

# Save and Share Chat History
if st.button("Save Chat History"):
    session_id = str(uuid.uuid4())[:8]
    with open(f"chat_history_{session_id}.json", "w") as f:
        json.dump(st.session_state.message_log, f)
    st.success(f"Chat saved! Share this session: `chat_history_{session_id}.json`")
