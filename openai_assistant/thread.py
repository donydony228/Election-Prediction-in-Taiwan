import openai
from dotenv import load_dotenv
import os
from config import settings

load_dotenv(override=True)
openai_api_key = os.environ.get(settings.openai_api_key)
client = openai.OpenAI(api_key=openai_api_key)
model = "gpt-4o"

def create_thread():
    thread = client.beta.threads.create()
    return thread.id