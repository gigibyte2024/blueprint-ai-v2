from abc import ABC, abstractmethod

from app.services.llm_service import generate_response
from app.utils.prompt_loader import load_prompt


class BaseAgent(ABC):

    def __init__(self, prompt_file: str):
        self.prompt_file = prompt_file

    def run(self, **kwargs):

        prompt = load_prompt(self.prompt_file)
        prompt = prompt.format(**kwargs)

        messages = [
            {
                "role": "system",
                "content": "You are an expert AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        response = generate_response(messages)

        return self.parse(response)

    @abstractmethod
    def parse(self, response):
        pass