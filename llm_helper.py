from turtledemo import __main__

from dotenv import load_dotenv
#when we call this function it will go to dotenv and that groq
#env variable will be set as env variable
from langchain_groq import ChatGroq
import os
load_dotenv()
# its going intp the groq cloud and then fetching the data, not running anything locally here
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="openai/gpt-oss-120b")

if __name__ == "__main__":
    response = llm.invoke("What are the two main ingredients in samosa")
    print(response.content)