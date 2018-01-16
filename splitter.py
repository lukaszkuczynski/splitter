from shapely.geometry import Point


class Splitter:

    def split_all_points(self, points, areas):
        areas_filled = dict()
        areas_list = list(areas)
        for point in points:
            area_name = point_to_area(point, areas_list)
            if area_name is None:
                raise Exception("area not found for point " + point.__str__())
            if area_name not in areas_filled:
                areas_filled[area_name] = []
            areas_filled[area_name].append(point)
        return areas_filled


def point_to_area(point, areas):
    for area in areas:
        p = Point((point['lat'], point['lng']))
        if area['shape'].contains(p):
            return area['name']