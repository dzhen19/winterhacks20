"""
This is a simple flask server
that handles requests from the frontend
"""
import overpy
import os
from flask import Flask, send_from_directory
#from grayscale import Grayscale

CURRENT_DIR = os.path.dirname(__file__)
client_folder = CURRENT_DIR + '/../client/build/'
app = Flask(__name__, static_folder=client_folder)

# account for imported request handlers
#app.register_blueprint(Grayscale)


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
  if path != "" and os.path.exists(client_folder + path):
    return send_from_directory(client_folder, path)
  else:
    return send_from_directory(client_folder, 'index.html')




"""
You input the four corners -- Min Latitude, Min Longitude, Max Lattitude and Max Longitude in that order -- as parameters.
The function then searches for nodes along all the streets in that area and clusters them. The function then returns 
a dictionary with index starting from 0 as key and a list of tuples containing lat and lon as value. The key represents a certain street in that neighborhood
and the value for that key corresponds to a list of tuples each of which represent the lat and lon of a node on that street.

Example:
    Dictionary {0: [(Decimal('39.9075698'), Decimal('-75.3455409')), (Decimal('39.9077168'), Decimal('-75.3466300')),
         (Decimal('39.9078800'), Decimal('-75.3478395')), (Decimal('39.9079213')}
"""
def getAllPossibleWays(minLat = 39.905688, minLon = -75.349770, maxLat = 39.908144, maxLon = -75.346066):
    api = overpy.Overpass()
    result = api.query(f"""
        way({str(minLat)}, {str(minLon)}, {str(maxLat)}, {str(maxLon)});
        (._;>;);
        out body;
        """)
    dic = dict()
    for i, way in enumerate(result.ways):
        lst = []
        for node in way.nodes:
            lst.append((node.lat, node.lon))
        dic[i] = lst
    return dic


if __name__ == '__main__':
  app.run(use_reloader=True, port=5000, threaded=True)
