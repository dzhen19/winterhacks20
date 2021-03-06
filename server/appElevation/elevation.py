# Have to pip install haversine, googlemaps, overpy
import googlemaps as gm
import haversine as hs
import overpy
import math
import requests
import simplejson as json
#import json
import server.appElevation.config as config #Config File
#import config as config #Python File

from array import *

api_key = config.api_key #Config file
#api_key = config.config.get_api("hello") #Python Version
#api_key = "" #Personal API
gmaps = gm.Client(key=api_key)

def nearestRoadBack(node): #2D array
    string = "https://roads.googleapis.com/v1/snapToRoads?path="
    first = False
    for i in node:
        if first == False:  # if n is the last index
            first = True
            string += str(i[0]) + "," + str(i[1])
        else:
            string+= "|" + str(i[0]) + "," + str(i[1])
    api = api_key
    string= string + f"&key={api}"
    res = requests.get(string)
    jsonScript = json.loads(res.text)
    newNode = []
    try:
        snappedPoints = jsonScript["snappedPoints"]
    except:
        snappedPoints = []
    for k, i in enumerate(snappedPoints):
        location = i["location"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        newNode.append([latitude, longitude])
    return newNode

def jsonGoogleCall(node): #node is a 2D Array
    string = "https://maps.googleapis.com/maps/api/elevation/json?locations="
    first = False
    for i in node:
        if first == False:  # if n is the last index
            first = True
            string += str(i[0]) + "," + str(i[1])
        else:
            string+= "|" + str(i[0]) + "," + str(i[1])
    api = api_key
    string= string + f"&key={api}"
    res = requests.get(string)
    jsonScript = json.loads(res.text)
    for k, i in enumerate(jsonScript["results"]):
        node[k].append(i["elevation"])
    return node

def getAllPossibleWays(minLat=39.905688, minLon=-75.349770, maxLat=39.908144, maxLon=-75.346066):
    api = overpy.Overpass()
    result = api.query(f"""
        way({str(minLat)}, {str(minLon)}, {str(maxLat)}, {str(maxLon)});
        (._;>;);
        out body;
        """)
    waysList = []
    for i, way in enumerate(result.ways):
        lst = []
        for node in way.nodes:
            lst.append([node.lat, node.lon])
        waysList.append(lst)
    return waysList


def destinationPoint(latlon, distance, bearing, radius=6371e3):
    # // sinφ2 = sinφ1⋅cosδ + cosφ1⋅sinδ⋅cosθ
    # // tanΔλ = sinθ⋅sinδ⋅cosφ1 / cosδ−sinφ1⋅sinφ2
    # // see mathforum.org/library/drmath/view/52049.html for derivation

    δ = distance / radius  # // angular distance in radians
    θ = math.radians(bearing)

    φ1 = math.radians(latlon[0])
    λ1 = math.radians(latlon[1])

    sinφ2 = math.sin(φ1) * math.cos(δ) + math.cos(φ1) * \
        math.sin(δ) * math.cos(θ)
    φ2 = math.asin(sinφ2)
    y = math.sin(θ) * math.sin(δ) * math.cos(φ1)
    x = math.cos(δ) - math.sin(φ1) * sinφ2
    λ2 = λ1 + math.atan2(y, x)

    lat = math.degrees(φ2)
    lon = math.degrees(λ2)

    return (lat, lon)


def boundingBox(latlon, radius):
    maxLat = destinationPoint(latlon, radius, 0)
    minLat = destinationPoint(latlon, radius, 180)
    minLon = destinationPoint(latlon, radius, 270)
    maxLon = destinationPoint(latlon, radius, 90)
    return minLat, minLon, maxLat, maxLon


def distanceBetweenTwoPoints(a, b):
    firstTuple = (a[0], a[1])
    secondTuple = (b[0], b[1])
    distance = hs.haversine(firstTuple, secondTuple)
    return (distance*1000)


def searchForNodes(personLat, personLong):
    searchThresholdLB = 75  # Lower Bound
    searchThresholdUB = 125  # Upper Bound
    overpassCallSearchRadius = 100  # Search Radius
    elevationThreshold = 0.1  # 0.1m of elevation for 10m of distance

    goodRoutes = []  # holds the good routes with elevation data. Each column has lat1, long1, elevation1, lat2, long2, elevation2, total distance, total change in elevation

    # API Calls to OverPass for Nodes. Need to store lat and long
    minLat, minLon, maxLat, maxLon = boundingBox(
        (personLat, personLong), overpassCallSearchRadius)
    # When Parsing in, use the overpassCallSearchRadius
    nodes = getAllPossibleWays(minLat[0], minLon[1], maxLat[0], maxLon[1])

    # API Calls to Roads API to snap nodes back onto road and then get elevation
    for node in nodes:
        node = nearestRoadBack(node)

    # API Calls to Roads API to snap nodes back onto road and then get elevation #Deprecated for optimisation as nearestRoadBack bundles Roads API Calls
    '''
    for node in nodes:
        for c in node:
            latLong = (c[0], c[1])
            result = gmaps.nearest_roads(latLong)
            if len(result) != 0:
                lat = result[0]["location"]["latitude"]
                lon = result[0]["location"]["longitude"]
                c[0] = lat
                c[1] = lon
                latLong = (c[0], c[1])
                #c.append(gmaps.elevation(latLong)[0]["elevation"]) #Deprecated for optimisation as jsonGoogleCall bundles elevation API calls
    '''

    #Combined Elevation Calls Go here
    for node in nodes:
        node = jsonGoogleCall(node)

    for node in nodes:
        for firstComparison in node:
            for secondComparison in node:
                if len(firstComparison) == 3 and len(secondComparison) == 3:
                    dis = distanceBetweenTwoPoints(
                        firstComparison, secondComparison)
                    if dis <= searchThresholdUB and dis >= searchThresholdLB:
                        elevation = firstComparison[2] - secondComparison[2]
                        first = firstComparison
                        second = secondComparison
                        if elevation < 0:
                            elevation = elevation * -1
                            third = second
                            second = first
                            first = third
                        # if elevation/dis > elevationThreshold:
                        newRoute = {}
                        newRoute["latitude1"] = first[0]
                        newRoute["longitude1"] = first[1]
                        newRoute["elevation1"] = first[2]
                        newRoute["latitude2"] = second[0]
                        newRoute["longitude2"] = second[1]
                        newRoute["elevation2"] = second[2]
                        newRoute["distance"] = dis
                        newRoute["delta_elevation"] = elevation
                        goodRoutes.append(newRoute)
    sortedRoutes = sorted(
        goodRoutes, key=lambda i: i['delta_elevation']/i['distance'], reverse=True)[0:11]
    # get the address again
    for route in sortedRoutes:
        route['address1'] = gmaps.reverse_geocode((route['latitude1'], route['longitude1']))[
            0]['formatted_address']
        route['address2'] = gmaps.reverse_geocode((route['latitude2'], route['longitude2']))[
            0]['formatted_address']
    return(sortedRoutes)

#if __name__ == "__main__":
    #node = [[39.905899, -75.336940], [39.905899, -75.336940], [39.905899, -75.336941]]
    #print(nearestRoadBack(node))
    #print(searchForNodes(39.905899, -75.336940))
    
    
