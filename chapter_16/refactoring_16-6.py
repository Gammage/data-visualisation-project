##refactoring exercise##
#loop that pulls data from all_eq_dicts uses variables for the magnitude,
#long, lat and title of each earthquake before appending these values to their
#appriopiate lists. this approach was chosen for clarity in how to pull up from a
#geoJSON file. not necessary in your code
#instead of using these temporarily variables pull each value from eq_dict and
#append it to the appropiate list in one line. doing so should shorten the 
#body of this loop to just four lines.
#

#list of information to store/reference on globe style datamap

from pathlib import Path
import json

import plotly.express as px

path = Path('./chapter_16/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding="utf-8") #windows can have diff defaults of encoding, explicit state here 
all_eq_data = json.loads(contents)

path = Path('./chapter_16/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

##refactoring exercise    
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
    
print(mags[:10])
print(lons[:5])
print(lats[:5])

title = "global earthquakes"
fig = px.scatter_geo(lat=lats, 
                     lon=lons,
                     size=mags, 
                     title=title,
                     color=mags, #determines colour of each point
                     color_continuous_scale='icefire', #tells which colour scale to use (viridis)
                     labels={'color':'magnitude'}, #takes a dict value.
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()