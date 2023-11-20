import openai
import os
import re


def extract_servings(text):
    """
LLM GENERATED
This function extracts the number of servings from the recipe text.
"""
    servings = re.search(r'(\d+)\s*servings', text)
    return servings.group(1) if servings else 'Servings information not available'


def separate_recipe(text):
    """
    LLM GENERATED
    This function separates the ingredients and instructions from the filtered text.
    """
    split_text = text.split('Cooking instructions:')
    ingredients = split_text[0].replace('Ingredients:', '').strip()
    instructions = split_text[1].strip()
    servings = extract_servings(text)
    return ingredients, instructions, servings


class GPT:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def filter(self, text):
        prompt_text = f"Take the following text which contains a recipe. Filter the text so only the ingredients and " \
                      f"the cooking steps remain. Return your result using the headings 'Ingredients:' and " \
                      f"'Cooking instructions:'This is the recipe: \n\n{text}"
        response = openai.Completion.create(model='gpt-3.5-turbo-instruct', prompt=prompt_text, max_tokens=2500)
        filtered_text = response.choices[0].text.strip()
        ingredients, instructions, servings = separate_recipe(filtered_text)
        return ingredients, instructions, servings

    def translate_recipe(self, filtered_recipe, selected_language):
        prompt_text = f'Translate the following recipe to {selected_language} and keep in mind to translate ' \
                      f'measuring units to units used in that language: \n\n{filtered_recipe}'
        response = openai.Completion.create(model='gpt-3.5-turbo-instruct', prompt=prompt_text, max_tokens=2500)
        translated_recipe_list = response.choices[0].text.strip().split('\n')
        return translated_recipe_list

