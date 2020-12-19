from server.appElevation.elevation import searchForNodes
from flask import Blueprint, request, jsonify, current_app
import googlemaps as gm
import haversine as hs
from server.appElevation.elevation import *
import overpy
import math
from array import *

Edges = Blueprint('edges', __name__)

@Edges.route("/api/edges", methods=['GET'])
def search():
    personLat = float(request.args.get('lat'))
    personLong = float(request.args.get('lng'))
    goodRoutes = searchForNodes(personLat, personLong)
    return jsonify({'routes': goodRoutes})
