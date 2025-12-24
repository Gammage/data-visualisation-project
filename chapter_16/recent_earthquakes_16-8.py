##recemt earthquakes exercise##

import plotly.express as plt
import json
from pathlib import Path

#loads will convert a json string to a python object
#even though it sjson python only understands it as a string until that point

path = Path("./chapter_16/eq_data/eq_data_30_day_last.geojson")
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

path = Path("./chapter_16/eq_data/readable_eq_30_day.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
longs = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts]
eq_title = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

title = all_eq_data['metadata']['title']

fig = plt.scatter_geo(lat=lats,
                      lon=longs,
                      size=mags,
                      title=title,
                      color=mags,
                      labels={"color":"magnitude"},
                      projection="natural earth",
                      hover_name=eq_title)

fig.show()

