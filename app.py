import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun 
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from dotenv import load_dotenv


# Dont Know
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Arxis and Wikipedia API Wrappers
api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=250)
arxiv=ArxivQueryRun(
    api_wrapper=api_wrapper_arxiv,
)

api_wrapper_wiki=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=250)
wiki=WikipediaQueryRun(
    api_wrapper=api_wrapper_wiki,
)

# Search through internet use duckduckgo
search=DuckDuckGoSearchRun(
    name="Search"
)


st.title("LangChain Chat with search")


# In this we are using 'streamlitcallbackhandler' to display the thoughts and actions of the agent in real-time.
# This is useful for debugging and understanding how the agent is reasoning about the task.



# sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Groq API Key", type="password")

# Gentle reminder if missing
if not api_key:
    st.sidebar.info("Please enter your Groq API Key above to enable the agent.")


# What is session state?
# https://docs.streamlit.io/knowledge-base/tutorials/session-state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"assistant", "content":"Hello! I am a LangChain agent who can search from the internet. How can I help you today?"},
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Prompt Create
if prompt:=st.chat_input(placeholder="What is machine learning?"):
    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Block if API key absent
    if not api_key:
        warning_msg = "Please enter your Groq API Key in the sidebar before asking questions."
        st.chat_message("assistant").write(warning_msg)
        st.session_state.messages.append({"role": "assistant", "content": warning_msg})
        st.stop()

    # Provide key via environment (current langchain_groq expects GROQ_API_KEY)
    os.environ["GROQ_API_KEY"] = api_key
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        streaming=True,
    )
    tools = [arxiv, wiki, search]

    # Initialize the agent with the LLM and tools 
    # ZERO_SHOT_REACT_DESCRIPTION does not depend on history
    # create_openai_tools_agent vs initialize_agent
    search_agent=initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        handling_parsing_errors=True,
    )
    # StreamlitCallbackHandler used to display the agent's thoughts and actions in real-time

    with st.chat_message("assistant"):
        # Use StreamlitCallbackHandler to display the agent's thoughts and actions in real-time
        st_cb= StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response=search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
        st.write("Response:", response)





































