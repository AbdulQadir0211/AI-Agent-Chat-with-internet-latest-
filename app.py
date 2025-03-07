import streamlit as st
from pydantic import BaseModel
from typing import List
from agent import get_response_from_llm

# Define allowed model names
ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# Define RequestState Model
class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("🤖 AI Chatbot with LangGraph")

# Sidebar for settings
st.sidebar.header("Chat Settings")
model_name = st.sidebar.selectbox("Select Model", ALLOWED_MODEL_NAMES)
system_prompt = st.sidebar.text_area("System Prompt", "You are a helpful assistant.")
allow_search = st.sidebar.checkbox("Enable Web Search", value=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if user_input := st.chat_input("Type your message..."):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Create request object
    request = RequestState(
        model_name=model_name,
        system_prompt=system_prompt,
        messages=[msg["content"] for msg in st.session_state.chat_history],
        allow_search=allow_search
    )
    
    # Get AI response
    response = get_response_from_llm(request.model_name, request.messages, request.allow_search, request.system_prompt)
    
    # Display AI response
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
