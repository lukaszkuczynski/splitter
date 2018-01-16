from shapely.geometry import Point


def point_to_area(point, areas):
    for area in areas:
        p = Point((point['lat'], point['lng']))
        if area['shape'].contains(p):
            return area['name']