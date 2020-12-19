from server.appElevation.elevation import searchForNodes
from flask import Blueprint, request, jsonify, current_app
import googlemaps as gm
import haversine as hs
from server.appElevation.elevation import *
from array import *

Edges = Blueprint('edges', __name__)

@Edges.route("/api/edges", methods=['GET'])
def search():
    current_app.logger.info("API queried!")
    personLat = float(request.args.get('lat'))
    personLong = float(request.args.get('lng'))
    goodRoutes = searchForNodes(personLat, personLong)
    current_app.logger.info(goodRoutes)
    return jsonify({'routes': goodRoutes})
