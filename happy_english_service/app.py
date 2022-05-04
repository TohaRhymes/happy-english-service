import flask
from happy_english_service import database

app = flask.Flask(__name__, template_folder='../templates')


@app.route('/')
def start():
    return flask.render_template('index.html')


@app.route('/search')
def search():
    phrase = flask.request.args.get('phrase')
    fragments, colnames = database.search(phrase, 'database.sqlite')
    return flask.render_template('record.html', records=fragments, colnames=colnames)
