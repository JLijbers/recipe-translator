import openai
import os


class GPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def filter(self, text):
        prompt_text = f"Take the following text which contains a recipe. Filter the text so only the ingredients and " \
                      f"the cooking steps remain. Return them in two separate strings." \
                      f"This is the recipe: \n\n{text}"
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            max_tokens=2500
        )
        filtered_recipe = response.choices[0].text.strip()
        return filtered_recipe

    def translate_recipe(self, filtered_recipe, selected_language):
        # Enhanced prompt for better translation
        prompt_text = f"Translate the following recipe to {selected_language} and keep in mind to translate measuring" \
                      f" units to units used in that language: \n\n{filtered_recipe}"
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            max_tokens=2500
        )
        translated_recipe = response.choices[0].text.strip()
        return translated_recipe
