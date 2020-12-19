"""
This is a simple flask server
that handles requests from the frontend
"""
import overpy
import os
from flask_simple_geoip import SimpleGeoIP
from flask import Flask, send_from_directory, jsonify
from server.api import Edges

CURRENT_DIR = os.path.dirname(__file__)
client_folder = CURRENT_DIR + '/../client/build/'
app = Flask(__name__, static_folder=client_folder)

# account for imported request handlers
app.register_blueprint(Edges)


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(client_folder + path):
        return send_from_directory(client_folder, path)
    else:
        return send_from_directory(client_folder, 'index.html')
