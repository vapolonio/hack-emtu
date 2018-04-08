import json
import requests

from flask import Flask, jsonify, make_response, request, abort
from settings.constants import API_KEY_MAPS, API_VERSION

server = Flask(__name__)

#rotas
@server.route('/', methods=['GET'])
def api_version():
    return 'api version: ' + API_VERSION

@server.route('/buscar', methods=['POST'])
def query_traffic():
    print(request.args.get('origem'))
    print(request.args.get('destino'))
    # search_direction(origem, destino)
    return 'mapa do onibus'






def startWebserver():
    server.run(threaded=True, debug=True, use_reloader=False)

startWebserver();
