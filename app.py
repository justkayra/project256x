from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


def get_user_lang(lang):
    pass


@app.route('/lang', methods=["POST"])
def change_lang():
    lang = request.fprm('lang')
    language = get_user_lang(lang)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
