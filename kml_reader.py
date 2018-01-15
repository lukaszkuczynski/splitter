from fastkml import kml

def read_kml(filepath):
    with open(filepath, 'rb') as f:
        k = kml.KML()
        kml_doc = f.read()
        k.from_string(kml_doc)
        documents = list(k.features())
        for doc in documents:
            print(doc)
            for placemark in doc.features():
                print(placemark)



if __name__ == '__main__':
    read_kml('areas.kml')