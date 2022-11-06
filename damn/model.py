"""Database model."""

from shapely import wkb
from enum import Enum

##############################################################################
### DATABASE OBJECTS
##############################################################################
class Line:
    osm_id = None
    count = 0
    avoided_count = 0
    chosen_count = 0
    parsed_coordinates = None
    
    def __init__(self, osm_id, damn_way_line_string) -> None:
        self.osm_id = osm_id
        self.parsed_coordinates = self.parseCoordinates(damn_way_line_string)

    def parseCoordinates(self, damn_way_line_string): 
        """ Parses a postgis LineString to a list of latitude and longitude coordinates."""
        point_list = wkb.loads(damn_way_line_string, hex=True)
        print(point_list.coords[:])

class DeliveryTrip:
    """An entity representing a delivery trip done by a Wolt partner."""
    id = None
    vehicle_type = None
    parsed_coordinates = None
    shortest_path = None

    def __init__(self, id, vehicle_type, parsed_coordinates) -> None:
        self.id = id
        self.vehicle_type = vehicle_type
        self.parsed_coordinates = parsed_coordinates

##############################################################################
### MISC.
##############################################################################
class VehicleType(Enum):
    BICYCLE = 'bicycle'
    E_BICYCLE = 'e-bicycle'
    CAR = 'car'
    E_SCOOTER = 'e-scooter'
    MOTORCYCLE = 'motorcycle'
    ON_FOOT = 'on foot'
    HOVERBOARD = 'hoverboard'
    OTHER = 'other'

class Incident(Enum):
    CLOSE_PASS = 'Close pass'
    CAR_DOOR = 'Card door opened'
    DODGED = 'Dodging and object'
    OTHER = 'Other'
