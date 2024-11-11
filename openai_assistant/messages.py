import openai, logging
from dotenv import load_dotenv
import os
from config import settings

load_dotenv(override=True)
openai_api_key = os.environ.get(settings.openai_api_key)
client = openai.OpenAI(api_key=openai_api_key)
model = "gpt-4o"

def insert_message(thread_id: str, role: str, content: str):
    logging.info(f"insert_message: {thread_id}, {role}, {content}")
    client.beta.threads.messages.create(thread_id=thread_id, role=role, content=content)