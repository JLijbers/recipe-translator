import openai
import os

class GPTTranslator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def translate(self, text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{text}\n\nSelect the recipe and ingredients from the text. Then translate to Dutch:",
            temperature=0.5,
            max_tokens=1000
        )
        return response.choices[0].text.strip()
