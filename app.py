from flask import Flask, render_template, request
from scraper import Scraper
from translator import GPTTranslator
from langdetect import detect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        scraper = Scraper(url)
        recipe_text = scraper.get_data()
        selected_language = request.form.get('language')
        translator = GPTTranslator()
        translated_text = translator.translate(recipe_text, selected_language)
        return render_template('index.html', recipe_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
