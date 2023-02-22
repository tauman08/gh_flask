
from datetime import time
from flask import Flask, g
from flask import request

app = Flask(__name__)

@app.route('/<string:search>', methods=['GET','POST'])
def index(search: str):
    name = request.args.get('search',None)
    if request.method == 'GET':
        return f'Hello, {search}'
    elif request.method == 'POST'
        return 'POST'


@app.before_request
def process_before_request():

    g.start_time = time()


@app.after_request
def process_after_request(responce):

    if hasattr(g,"start_time"):
        responce.headers["process-time"] = time() - g.start_time

    return responce


@app.errorhandler(404)
def handler_404(error):
    app.logger.error(error)
    return '404'