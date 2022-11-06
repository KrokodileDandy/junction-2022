#!/usr/bin/python

"""Program entrypoint."""

import db_manager as db
from model import Line, DeliveryTrip, VehicleType

if __name__ == '__main__':
    query = 'SELECT osm_id, damn_way_line_string FROM planet_osm_line LIMIT 10;'
    a = db.run_query(query)[0]
    model = Line(a[0], a[1])
    trip = DeliveryTrip(0, VehicleType.BICYCLE, model.parsed_coordinates)