import openai
import os


class GPTTranslator:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def translate(self, text, selected_language):
        # Enhanced prompt for better translation
        prompt_text = f"Translate the following recipe text to {selected_language} and keep in mind to translate " \
                      f"measuring units to units used in that country:\n\n{text}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_text,
            max_tokens=1000
        )
        return response.choices[0].text.strip()
