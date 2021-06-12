from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

LANGUAGES = {
    'en': 'English',
    'ru': 'Русский'
}

@app.route('/')
def hello_world():
    return 'Hello World!'


def get_user_lang(lang):
    pass


@app.route('/lang', methods=["POST"])
def change_lang():
    lang = request.form['lang']
    #language = request.get_user_lang(lang)
    return 'Hello World!' + LANGUAGES[lang]


if __name__ == '__main__':
    app.run()
