from pandas.io.json import json_normalize
import folium
from geopy.geocoders import Nominatim
import requests
import pandas as pd
import folium
from folium import plugins
import math

geolocator = Nominatim(user_agent="foursquare_agent")

ny_location = geolocator.geocode("New York, USA")
ny_latitude = ny_location.latitude
ny_longitude = ny_location.longitude

print("New York latitude: ", ny_latitude, ", New York longitude: ", ny_longitude)

locationnew= pd.DataFrame(columns=['LATITUDE', 'LONGITUDE','NAME'])
lat = float(input("Enter the latitude of your place: "))
lon = float(input("Enter the longitude of your place: "))

link='newyorkcoffeewithdetails.csv'
df=pd.read_csv(link,error_bad_lines=False)
df.head()


for i in range(len(df)):
    R = 6373.0

    lat1 = math.radians(lat)
    lon1 = math.radians(lon)
    lat2 = math.radians(df["location.lat"].iloc[i])
    lon2 = math.radians(df["location.lng"].iloc[i])

    dlon = lon2 - lon1

    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance =R*c
    if (distance<1.8):
        locationnew=locationnew.append({'LATITUDE' : df["location.lat"].iloc[i],'LONGITUDE' : df["location.lng"].iloc[i],"NAME": df["name"].iloc[i]} , ignore_index=True)

print(locationnew.head())

new_york_location=[40.730610,-73.935242]
m=folium.Map(new_york_location,zoom_start=11,width="%100",height="%100")
for i in range(len(locationnew)):
    folium.Marker(locationnew.loc[i, ['LATITUDE','LONGITUDE']],
                  tooltip=locationnew["NAME"].iloc[i],
                 ).add_to(m)
m

