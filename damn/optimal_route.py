"""
This module contains code for retrieving the optimal route for a delivery
using the Graphopper Routing API.
"""

import requests

api_key = 'api_key' # example key

def coordinate_to_string(coordinate) -> str:
    return str(coordinate[0]) + ',' + str(coordinate[1])

def validate_profile(profile):
    valid_options = list('foot', 'bike', 'scooter', 'car')
    if profile in valid_options:
        return True
    else:
        raise Exception('Invalid profile (transport mode): ' + profile)

def construct_url(startPoint, endPoint, profile) -> str:
    point1 = coordinate_to_string(startPoint)
    point2 = coordinate_to_string(endPoint)
    validate_profile(profile)
    url = 'https://graphhopper.com/api/1/route?point=%s&point=%s&profile=%s&locale=en&calc_points=true&key=%s'%(point1, point2, profile, api_key)
    return url

def get_optimal_route(lat, long, transport_mode):
    url = construct_url(lat, long, transport_mode)
    response = requests.get(
        url,
        params=None
    )
    print(response)

