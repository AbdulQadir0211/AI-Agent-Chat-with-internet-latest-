# Setup UI with streamlit (model,system prompt,allow search , query)


import streamlit as st
st.set_page_config(page_title = "LangGraph Agent UI", layout = "wide")
st.title("AI chatbot Agents : Chat via internet")
st.write("Interact with AI Agensts on latest data via internet")

system_prompt =  st.text_area("Define your AI Agents(Role)",height=70,placeholder="Type your system prompt here...")

model_names = ["llama-3.3-70b-versatile","llama-3.1-8b-instant","mixtral-8x7b-32768"]

selected_model = st.selectbox("Select a model: ", model_names)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter Your Query: ",height=150,placeholder="Ask anything")

API_URL = "http://127.0.0.1:9999/chat"


if st.button("Ask Agent!"):
    if user_query.strip():
        # Get response from backend and show here
        ## Connect with backen using fastapi
        
        import requests
        payload = {
            "model_name": selected_model,
            "query": [user_query],
            "allow_search": allow_web_search,
            "system_prompt": system_prompt,
        }


        response = requests.post(API_URL,json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"***final response***{response_data}")

                              
