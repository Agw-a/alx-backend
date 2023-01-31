#!/usr/bin/env python3
'''A basic flask app
'''
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config():
    '''configure local settings
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''get locale from webpage
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_home():
    ''' Define defaults and renders
    '''
    return render_template('2-index.html')
