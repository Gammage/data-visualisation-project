#Mapping global datasets: GeoJSON format
#GeoJSON format is handled with it using json module (no shit)
#using plotlys scatter_geo() plot, youl create visualisations that 
#clearly show the global distribution of earthquakes

#exmaining geoJSON Data

from pathlib import Path
import json

#read as a string and convert into a python object
path = Path('./chapter_16/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding="utf-8") #windows can have diff defaults of encoding, explicit state here 
all_eq_data = json.loads(contents)

#create a more readable version of the data file
path = Path('./chapter_16/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

#in this example (see output), entire dataset is converted into a single dictionary.
#we assign it to new path as above
#json.dumps() function can take an optional indent function which tells it how much to indent
#nested elements in the data structure.

#json fileformat
#first part is metadata: tells us when the data file was generated and where we can find the 
#data online
    #also gives a human readable title and number of earthquakes inc in file
    #this geojson file has a structure helpful for location based data
        #info is stored in a list associated with the key features
        #because file contains earthquake data, data is in list for mwhere
        #every item in lists corresponds to a single earthquake
    #magnititude of earthquake with the key mag
    #title
    #geometry = where it occured
    
    #understanding conventions of data is important. in geospatial stuff,
        #longitude first and then latitude, corresponds to x,y in this dataset
        
# examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

##extracting magnitudes##
##extracting location data##
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(lons[:5])
print(lats[:5])

#building a world map