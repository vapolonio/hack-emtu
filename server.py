import json
import requests

from flask import Flask, jsonify, make_response, request, abort
from settings.constants import API_KEY_MAPS, API_VERSION

server = Flask(__name__)

#rotas
@server.route('/', methods=['GET'])
def api_version():
    return 'api version: ' + API_VERSION





def startWebserver():
    server.run(threaded=True, debug=True, use_reloader=False)

startWebserver();
