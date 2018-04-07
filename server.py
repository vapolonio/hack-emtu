import json
import requests

from flask import Flask, jsonify, make_response, request, abort

server = Flask(__name__)


@server.route('/', methods=['GET'])
def api_version():
    return 'alpha'

def startWebserver():
    server.run(threaded=True, debug=True, use_reloader=False)

startWebserver();
