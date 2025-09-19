# 🔎 Langchain - Chat with Search

A **Streamlit-based AI Chatbot** powered by **LangChain** and **Groq LLMs**.  
It can fetch **Wikipedia articles**, **Arxiv research papers**, and perform **web searches (DuckDuckGo)** in real time.  
Built with an interactive ChatGPT-like UI using `st.chat_message` and `st.chat_input`.

## 🚀 Features

- ChatGPT-like UI with Streamlit
- Integration with **Groq LLMs** (Llama 3.1 8B Instant)
- Web search via DuckDuckGo
- Research paper summaries via Arxiv
- Knowledge queries via Wikipedia
- Agent powered by `ZERO_SHOT_REACT_DESCRIPTION`
- Live agent thoughts/actions visible with `StreamlitCallbackHandler`

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit** – UI framework
- **LangChain** – Agent & tools management
- **Groq API** – LLM provider
- **DuckDuckGo Search API** – Web results
- **Arxiv API** – Research papers
- **Wikipedia API** – General knowledge
- **python-dotenv** – Environment variable management

## 📂 Project Structure

├── app.py # Main Streamlit app  
├── requirements.txt # Python dependencies  
├── .env # Environment variables (API key)  
└── README.md  

## ⚙️ Setup & Installation

1. **Clone this repository**
    ```
    git clone https://github.com/your-username/3.Search-Engine-With-Tools-Agent.git
    cd 3.Search-Engine-With-Tools-Agent
    ```

2. **Create a virtual environment**
    ```
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    ```

3. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **Configure environment variables**

    - Create a `.env` file:
        ```
        GROQ_API_KEY=your_groq_api_key_here
        ```

## ▶️ Usage (Local)

Run the app locally:

streamlit run app.py

- Open [http://localhost:8501](http://localhost:8501) in your browser  
- Enter your query in the chat box  
- The agent will decide whether to use:
  - Wikipedia  
  - Arxiv  
  - DuckDuckGo     

## 📜 License

This project is licensed under the MIT License.