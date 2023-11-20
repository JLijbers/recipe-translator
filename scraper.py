from bs4 import BeautifulSoup
import requests

class Scraper:

    def __init__(self, url):
        self.url = url

    def get_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text

    def get_servings(self):
        """
        LLM GENERATED
        This function extracts the number of servings from the recipe text.
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        servings = soup.find('span', {'class': 'servings'}).text
        return servings