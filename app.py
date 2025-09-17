import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun

from langchain.agents import initialize_agent, AgentType

from langchain.callbacks import StreamlitCallbackHandler

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## Arxiv & Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

## title of page
st.title("🔎 Langchain - Chat with Search")
"""
in this example, we are using "StreamlitCallbackHandler" to display the thoughts and actions of an Agent in an interactive streamlit applications
"""

## Sidebar
# st.sidebar("Settings")
# api_key = st.sidebar.text_input("Enter your GROQ API key: ", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"assistant", "content":"Hii! I'm a chatbot who can search the web. How can I assist you?"}
    ]

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

if prompt:=st.chat_input(placeholder="How can I assist you?"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name = "llama-3.1-8b-instant", streaming=True)
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_error=True)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({'role':'assistant', "content":response})
        st.write(response)