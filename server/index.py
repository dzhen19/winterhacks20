"""
This is a simple flask server
that handles requests from the frontend
"""
import os
from flask import Flask, send_from_directory
from upload import Upload
from grayscale import Grayscale
from gif import Gif

CURRENT_DIR = os.path.dirname(__file__)
client_folder = CURRENT_DIR + '/../client/build/'
app = Flask(__name__, static_folder=client_folder)

# account for imported request handlers
app.register_blueprint(Upload)
app.register_blueprint(Grayscale)
app.register_blueprint(Gif)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
  if path != "" and os.path.exists(client_folder + path):
    return send_from_directory(client_folder, path)
  else:
    return send_from_directory(client_folder, 'index.html')


if __name__ == '__main__':
  app.run(use_reloader=True, port=5000, threaded=True)
