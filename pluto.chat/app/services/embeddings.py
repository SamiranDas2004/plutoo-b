from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"))

def create_embedding(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return response.data[0].embedding
