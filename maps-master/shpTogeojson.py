import sys

#pip install pyshp
import shapefile
# read the shapefile
reader = shapefile.Reader(sys.argv[1])
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature",geometry=geom, properties=atr))

# write the GeoJSON file
from json import dumps
geojson = open(sys.argv[2], "w")
geojson.write(dumps(buffer, indent=1) + "\n")
geojson.close()
