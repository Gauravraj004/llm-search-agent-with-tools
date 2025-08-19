# 🤖 LangChain Search Agent with Groq LLM  

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

An **AI-powered research assistant** built with **LangChain**, **Groq LLMs**, and **Streamlit**.  
This chatbot can search **Arxiv** for research papers, fetch **Wikipedia** summaries, and perform **live web searches** using DuckDuckGo — all inside a clean, interactive web app.  

---

## ✨ Features
- 🤖 **Conversational AI** using Groq’s `llama-3.3-70b-versatile` model  
- 📚 **Arxiv Integration** – fetch research paper summaries  
- 📝 **Wikipedia Lookup** – concise encyclopedia entries  
- 🌐 **Web Search** – real-time answers via DuckDuckGo  
- 🎛️ **Streamlit UI** – simple, interactive chat experience  


---

## 💡 Use Cases
- Quickly retrieve summaries of **academic papers**  
- Get **reliable encyclopedia information** from Wikipedia  
- Perform **live internet searches** for up-to-date knowledge  
- Chat with a **reasoning LLM agent** that decides when to use tools  

---

## 🛠️ Technologies
- Python  
- Streamlit  
- LangChain  
- Groq LLMs  
- Arxiv API / Wikipedia API  
- DuckDuckGo Search  

---

## 📂 Project Structure

- app.py              # Main Streamlit application

- requirements.txt    # Project dependencies

- tools_agents.ipynb  # Notebook for experiments

- README.md           # Project documentation



---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/llm-search-agent-with-tools.git
cd llm-search-agent-with-tools

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

---
## 🚀 Run the App
streamlit run app.py

