from flask import Flask, request, jsonify
from flask_babel import Babel
from flask_cors import cross_origin

app = Flask(__name__)
babel = Babel(app)
supported = app.config.get('BABEL_SUPPORTED_LOCALES', ['en', 'ru', 'pt'])
default = app.config.get('BABEL_DEFAULT_LOCALE', 'en')

motto = {'en': 'Semantyca of your business', 'ru': 'Семантика вашего бизнеса', 'pt': 'Semantyca do seu negócio'}
home_button = {'en': 'Home', 'ru': 'Домой', 'pt': 'Para casa'}
tasks_button = {'en': 'Tasks', 'ru': 'Задачи', 'pt': 'Tarefas'}

@babel.localeselector
def get_locale():
    locale = request.accept_languages.best_match(supported, default)
    return 'pt'


@app.route('/home', methods=["GET"])
@cross_origin(origin='*')
def change_lang_default():
    return change_lang('en')


@app.route('/home/<lang>', methods=["GET"])
@cross_origin(origin='*')
def change_lang(lang):
    lang == request.view_args['lang']
    page = {
        'lang': lang,
        'name': 'Semantyca',
        'motto': motto.get(lang),
        'subMotto': 'This is an inception\nAll you get is this web site',
        'menu': {
            'home': home_button.get(lang),
            'tasks': tasks_button.get(lang)
        }
    }
    return jsonify(page)


@app.route('/login', methods=["POST"])
@cross_origin(origin='*')
def login():
    return 'Hello login!'


if __name__ == '__main__':
    app.run()
