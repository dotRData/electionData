import json
from pprint import pprint

json_data = open('cordJson.json').read()
data     =  json.loads(json_data)

for state in data:
    stateName = state['properties'][state['properties'].keys()[0]]
    for cords in state['geometry']['coordinates']:
        for lon,lat in cords[0]:
            print stateName, lon,lat