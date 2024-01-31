#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, g


app = Flask(__name__)


class Config:
    """App Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
@babel.localeselector
def get_locale():
    """return languages"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])



def get_user():
    ''' return the right dictionary '''
    Id = request.args.get('login_as')
    if Id and int(Id) in users:
        return users[int(Id)]
    else:
        return None

@app.before_request
def before_request():
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """return template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run
