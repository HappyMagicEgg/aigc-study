import os
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv('.env')

llm = OpenAI(api_key=os.getenv("OPENAI_KEY"),
            model_name="gpt-3.5-turbo-instruct",
            n=2, temperature=0.3
        )
str = llm.invoke("给我讲一个笑话")

print(str)