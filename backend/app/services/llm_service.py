from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_response(messages, model=None, temperature=0.3):
    completion = client.chat.completions.create(
        model=model or settings.MODEL_NAME,
        messages=messages,
        temperature=temperature,
    )

    return completion.choices[0].message.content