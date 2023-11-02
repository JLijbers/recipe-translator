import openai
import os


class GPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def filter(self, text):
        prompt_text = f"Take the following text which contains a recipe. Filter the text so only the ingredients and " \
                      f"the cooking steps remain. Return your result using the headings 'Ingredients:' and " \
                      f"'Cooking instructions:'" \
                      f"This is the recipe: \n\n{text}"
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            max_tokens=2500
        )
        filtered_text = response.choices[0].text.strip()
        ingredients, instructions = self.separate_recipe(filtered_text)
        return ingredients, instructions

    def separate_recipe(self, text):
        """
        LLM GENERATED
        This function separates the ingredients and instructions from the filtered text.
        """
        split_text = text.split('Cooking instructions:')
        ingredients = split_text[0].replace('Ingredients:', '').strip()
        instructions = split_text[1].strip()
        return ingredients, instructions

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
