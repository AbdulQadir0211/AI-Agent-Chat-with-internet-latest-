# Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

from agent import get_response_from_llm


class RequestState(BaseModel):
    model_name: str
    #model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool




# Setup AI Agent from FrontEnd Request

from fastapi import FastAPI

ALLOWED_MODEL_NAMES = ["llama-3.3-70b-versatile","llama-3.1-8b-instant","mixtral-8x7b-32768"]

app = FastAPI(title= "LangGraph AI agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):

    
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"Error, Please select a valid model"}
    
    # Create ai agent's response

    llm_id = request.model_name
    messages = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt

    response = get_response_from_llm(llm_id,messages,allow_search,system_prompt)
    return response



## Run app and explore swagger UI Docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host = "127.0.0.1",port = 9999)