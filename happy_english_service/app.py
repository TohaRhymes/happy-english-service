import flask
from happy_english_service import database

app = flask.Flask(__name__, template_folder='../templates')


@app.route('/')
def start() -> str:
    return flask.render_template('index.html')


@app.route('/search')
def search() -> str:
    phrase = flask.request.args.get('phrase')
    fragments, colnames = database.search(phrase, 'database.sqlite')
    print(fragments)
    print(colnames)
    return flask.render_template('record.html', records=fragments, colnames=colnames)
