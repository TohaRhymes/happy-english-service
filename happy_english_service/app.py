import dataclasses
import json
import flask
from happy_english_service import database
import pandas as pd

app = flask.Flask(__name__, template_folder='../templates')


@app.route('/search')
def search():
    phrase = flask.request.args.get('phrase')
    # TODO убрать в конфиг-файл
    fragments, colnames = database.search(phrase, 'database.sqlite')
    # colnames = ['content', 'link']
    return flask.render_template('record.html', records=fragments, colnames=colnames)
    # return flask.Response(fragments_json, status=200, mimetype='application/json')
