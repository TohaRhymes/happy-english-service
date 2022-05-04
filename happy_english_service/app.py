import dataclasses
import json
import flask
from happy_english_service import database

app = flask.Flask(__name__)


@app.route('/search')
def search():
    phrase = flask.request.args.get('phrase')
    print(phrase)
    # TODO убрать в конфиг-файл
    fragments = database.search(phrase, 'database.sqlite')
    print('hohohehe')
    fragments_json = json.dumps([dataclasses.asdict(fragment) for fragment in fragments])
    return flask.Response(fragments_json, status=200, mimetype='application/json')
