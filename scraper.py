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
