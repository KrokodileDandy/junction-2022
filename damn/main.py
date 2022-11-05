#!/usr/bin/python
import db_manager as db
from model import Line

if __name__ == '__main__':


    query = 'SELECT osm_id, damn_way_line_string FROM planet_osm_line LIMIT 10;'
    query2 = 'SELECT damn_way_line_string FROM planet_osm_line LIMIT 10;'
    a = db.run_query(query)[0]
    print(a)
    model = Line(a[0], a[1])