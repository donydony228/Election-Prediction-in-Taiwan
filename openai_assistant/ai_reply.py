import asyncio
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from config import settings

load_dotenv()

class OpenAIClient:
    def __init__(self, model: str = settings.default_openai_model):
        """
        Set up OpenAI client

        Args:
            model (str): The model name. Visit https://platform.openai.com/docs/models to get model names
        """

        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
        self.client = AsyncOpenAI(api_key=self.openai_api_key)
        self.model = model

    async def text_reply(self, prompt: str) -> str:
        """
        Ask the AI model to reply to the prompt

        Args:
            prompt (str): The prompt to ask the AI model
        Returns:
            str: The AI model's response, or an empty string if the model fails to respond
        """

        try:
            completion = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            response = completion.choices[0].message.content
            return response
        except Exception as e:
            print(e)
            return ""