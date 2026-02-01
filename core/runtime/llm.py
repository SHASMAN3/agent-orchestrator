from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def get_chat_model(model_name: str):
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=0.3
    )

def call_llm(prompt: str, model_name: str) -> str:
    chat_model = get_chat_model(model_name)

    response = chat_model.invoke(
        [HumanMessage(content=prompt)]
    )

    return response.content








