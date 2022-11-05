from shapely import wkb


class Line:
    osm_id = None
    count = 0
    avoided_count = 0
    chosen_count = 0
    parsed_coordinates = None
    
    def __init__(self, osm_id, damn_way_line_string) -> None:
        self.osm_id = osm_id
        self.damn_way_line = damn_way_line_string
        self.parsed_coordinates = self.parseCoordinates(damn_way_line_string)

    def parseCoordinates(self, damn_way_line_string): 
        # parse damn_way_line_string to a list of lat and long coordinates
        point_list = wkb.loads(damn_way_line_string, hex=True)
        print(point_list.coords[:])