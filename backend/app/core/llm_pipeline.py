import os
from langchain_groq import ChatGroq


def process_query(query):
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.environ.get("GROQ_API_KEY")
    )

    response = model.invoke(query)

    return response.content
