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
    """
    An entity representing a delivery trip done by a Wolt partner.
    
    Parameters
    ----------
    path: list()
        A list of Line objects, representing the path of the delivery.
    shortest_path: list()
        A list of Line objects, representing the shortest path between the
        start and end coordinate of the delivery.
    """
    id = None
    vehicle_type = None
    path: list() = None
    shortest_path: list() = None

    def __init__(self, id, vehicle_type, path) -> None:
        self.id = id
        self.vehicle_type = vehicle_type
        self.path = path

class Incident:
    """A near-miss incident during a DeliveryTrip."""
    id = None
    vehicle_type = None
    location = None
    description = None

    def __init__(self, id, vehicle_type, location, description):
        self.id = id
        self.vehicle_type = vehicle_type
        self.location = location
        self.description = description

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
