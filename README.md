# 🧠 DeepSeek Code Companion

## 🚀 Overview

DeepSeek Code Companion is an AI-powered coding assistant built using Streamlit, DeepSeek models, and LangChain. It helps with:

🐍 Python Debugging

📝 Code Explanation

🐞 Error Fixing Assistance

💡 Solution Optimization

The assistant allows users to chat with AI for coding help, execute Python code (if enabled), and even analyze previous executions.


## 🛠 Features

✔ Custom AI Personas 🎭

Beginner Guide 📖 – Simplified explanations for new programmers.

Debugger 🐞 – Focused on debugging and troubleshooting.

Optimized Coder ⚡ – Provides performance-optimized solutions.

✔ DeepSeek Model Support 🤖

Uses DeepSeek-R1 (1.5B & 3B) models for advanced coding assistance.

More models can be integrated in the future.

✔ Python Code Execution 🏗️

Available for Debugger & Optimized Coder personas.

Users can execute Python scripts and see results.

## 🎯 How to Run

🏗️ 1️⃣ Install Dependencies

pip install -r requirements.txt

🖥️ 2️⃣ Start the Streamlit App

streamlit run app.py

🎮 3️⃣ Use the AI Code Companion!

Select a DeepSeek model from the sidebar.

Choose an AI persona (Beginner, Debugger, Optimized Coder).

If applicable, enable Python execution.

Ask coding questions in the chat box.

✔ Chat History & Sharing 💾

Saves conversations to JSON.

Users can share their sessions.

## 🔄 Downloading DeepSeek Models with Ollama

Ollama allows you to easily download and use different DeepSeek models. Run the following commands to install and use them:

🔹 Download DeepSeek Models

ollama pull deepseek-r1:1.5b
ollama pull deepseek-r1:3b
download other models from : https://ollama.com/library/deepseek-coder

🔹 Run Ollama Locally

ollama serve

🔹 Check Available Models

ollama list

This ensures your app can use the required DeepSeek models for AI-based coding assistance.

## 🔧 Future Enhancements

📌 Add more DeepSeek models for better performance.📌 Improve multi-language support (C++, JavaScript, Java, etc.).📌 Enhance real-time AI suggestions while coding.
