from fastkml import kml
from shapely.geometry import LineString


def read_kml_areas(filepath):
    with open(filepath, 'rb') as f:
        k = kml.KML()
        kml_doc = f.read()
        k.from_string(kml_doc)
        documents = list(k.features())
        for doc in documents:
            for placemark in doc.features():
                area_name = print(placemark.name)
                area_shape = LineString(placemark.geometry)
                yield {"name": area_name, "shape": area_shape}
