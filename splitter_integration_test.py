from unittest import TestCase
from kml_reader import read_kml_areas
from splitter import point_to_area


class SplitterTestIntegration(TestCase):

    def test_splitter_can_guess_area_for_skytower(self):
        areas = read_kml_areas("areas.kml")
        skytower_coords = {
            'lat': 17.017166598,
            'lng': 51.089666308
        }
        area_found = point_to_area(skytower_coords, areas)
        self.assertIsNotNone(area_found)
