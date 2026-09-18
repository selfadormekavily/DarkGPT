import os
from langchain_groq import ChatGroq


def process_query(query):
    model = ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.7,
    )

    response = model.invoke(query)

    return response.content
