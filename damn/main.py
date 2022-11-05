#!/usr/bin/python
import db_manager as db

if __name__ == '__main__':


    query = 'SELECT osm_id, damn_way_line_string FROM planet_osm_line LIMIT 10;'
    print(db.run_query(query))
