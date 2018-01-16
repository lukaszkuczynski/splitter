from unittest import TestCase
from kml_reader import read_kml_areas
from splitter import point_to_area, Splitter


class SplitterTestIntegration(TestCase):

    def test_splitter_can_guess_area_for_skytower(self):
        areas = read_kml_areas("areas.kml")
        skytower_coords = {
            'lat': 17.019690,
            'lng': 51.094880
        }
        area_found = point_to_area(skytower_coords, areas)
        self.assertEquals(area_found, 'Gajowice 1')

    def test_splitter_does_the_map(self):
        areas = read_kml_areas("areas.kml")
        city_spots = [
            {"name": "skytower", "type": "shopping mall", "lat": 17.019690, "lng":51.094880},
            {"name": "Biedronka close to skytower", "type": "small shop", "lat":17.018921, "lng":51.097994},
            {"name": "Panorama Racławicka", "type": "historical building", "lat":17.044462, "lng": 51.110171},
            {"name": "Galeria Dominikańska", "type": "shopping mall", "lat":17.040685, "lng":51.108244},
        ]
        splitter = Splitter()
        assigned = splitter.split_all_points(city_spots, areas)
        self.assertTrue(len(assigned) == 2)
        self.assertIn('Rynek 1', assigned)
        self.assertIn('Gajowice 1', assigned)