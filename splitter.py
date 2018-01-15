from shapely.geometry import shape, Point

def point_to_area(point, areas):
    for area in areas:
        p = Point(point['lat'], point['lng'])
        # p = Point(point['lng'], point['lat'])
        print(area['shape'])
        if area['shape'].contains(p):
            return area['name']