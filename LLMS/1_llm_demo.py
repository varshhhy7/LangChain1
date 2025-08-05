import os
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENAI_API_KEY"),  
    model="deepseek/deepseek-chat"
)

question = input("Please ask the question: ")
response = llm.invoke(question)

print(response.content)
