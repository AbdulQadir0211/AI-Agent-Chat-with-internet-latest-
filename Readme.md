# LangGraph AI Agent

## Overview
This project is a FastAPI-based chatbot API using **LangGraph** and **Groq's AI models**. It allows users to select an AI model, send a chat message, and optionally enable a search tool for improved responses. The chatbot leverages the `ChatGroq` LLM and `TavilySearchResults` for search-based augmentation. The frontend is built using **Streamlit** for an interactive user experience.

## Features
- Supports **multiple AI models**: `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, and `mixtral-8x7b-32768`
- Uses **LangGraph's** `create_react_agent` for reasoning and tool usage.
- Includes **Tavily search tool** (optional) to fetch real-time data.
- Simple **FastAPI** backend for handling chat requests.
- **Streamlit frontend** for an easy-to-use UI.
- Easily deployable on **Hugging Face Spaces**, **Docker**, or a cloud server.

---
## Installation
### Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/langgraph-ai-agent.git
cd langgraph-ai-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root and add your API keys:
```plaintext
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Load the environment variables automatically:
```python
from dotenv import load_dotenv
load_dotenv()
```

---
## Usage
### Running the FastAPI Server
```bash
https://aiagentchatbot.streamlit.app/)
```
This will start the API server at `http://127.0.0.1:9999`

### Running the Streamlit Frontend
```bash
streamlit run frontend.py
```
This will launch a Streamlit UI where users can interact with the chatbot.

### API Endpoints
#### 1. Chat Endpoint
**URL:** `POST /chat`

**Request JSON:**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a helpful AI assistant",
  "messages": ["Hello, how are you?"],
  "allow_search": true
}
```

**Response JSON:**
```json
{
  "response": "Hello! How can I assist you today?"
}
```

#### 2. API Documentation
Once the server is running, visit the **Swagger UI** for interactive testing:
- **Swagger UI:** `http://127.0.0.1:9999/docs`
- **Redoc:** `http://127.0.0.1:9999/redoc`

---
## Project Structure
```
langgraph-ai-agent/
│── app.py               # Main FastAPI application
│── agent.py             # LLM and AI agent logic
│── frontend.py          # Streamlit UI for chatbot
│── requirements.txt     # Python dependencies
│── .env                 # API keys (ignored in Git)
│── README.md            # Project documentation
```

---
## Deployment
You can deploy the API on **Hugging Face Spaces**, **Docker**, or a cloud provider.

### Docker Deployment
1. Create a `Dockerfile`:
```Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
```

2. Build and run the Docker container:
```bash
docker build -t langgraph-ai-agent .
docker run -p 80:80 langgraph-ai-agent
```

---
