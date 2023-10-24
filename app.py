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
        detected_language = detect(recipe_text)
        translator = GPTTranslator()
        translated_text = translator.translate(recipe_text)
        return render_template('index.html', recipe_text=translated_text, detected_language=detected_language)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
