import os

from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("")
TAVILY_API_KEY = os.getenv("")


# Setup LLM and tools
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages.ai import AIMessage

#groq_llm = ChatGroq(model = "llama-3.3-70b-versatile")


#search_tool = TavilySearchResults(max_results =2)


## Setup ai agent with search tools 
from langgraph.prebuilt import create_react_agent

#action_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_llm(llm_id,query,allow_search,system_prompt):

    groq_llm = ChatGroq(model = llm_id)

    search_tool = [TavilySearchResults(max_results =2)] if allow_search else []
    

    agent = create_react_agent(
        model = groq_llm,
        tools = search_tool,
        state_modifier = system_prompt
    )

    

    state = {"messages":query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message,AIMessage)]
    return ai_message[-1]