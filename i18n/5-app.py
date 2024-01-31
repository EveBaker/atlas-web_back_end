#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
def get_locale():
    """return language"""
    return request.args.get('locale', request.accept_languages
                            .best_match(app.config['LANGUAGES']))


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """return template"""
    return render_template('4-index.html', gettext=gettext)


if __name__ == '__main__':
    app.run
