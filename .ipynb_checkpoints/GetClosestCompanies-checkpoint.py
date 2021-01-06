import pandas as pd
import math

df = pd.read_csv(r"C:\Users\MONSTER\Desktop\newyorkcoffeewithdetails.csv", error_bad_lines=False)

distance_dict = {}

lat_input = float(input("Latitude : "))  # User's latitude and longitude
lon_input = float(input("longitude : "))

for i in range(len(df)):  # I take latitutude and longitude for every buisness

    # our latitude and longitude of surroindings
    lat = math.radians(df["location.lat"].iloc[i])
    lon = math.radians(df["location.lng"].iloc[i])

    R = 6373.0  # Diameter of earth

    distance_lon = lon2 - lon1
    distance_lat = lat2 - lat1

    # Haversine Formula for finding distance between two geographical locations in earth

    a = math.sin(distance_lat / 2) ** 2 + math.cos(lat_input) * math.cos(lat) * math.sin(distance_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    distance_dict[i] = distance

sorted_values = sorted(distance_dict.values())  # Sort the values
sorted_distance_dict = {}

# I sort my dictionary in terms of values from small to big
for i in sorted_values:
    for k in distance_dict.keys():
        if distance_dict[k] == i:
            sorted_distance_dict[k] = i
            break

print(sorted_distance_dict)

location_stats = pd.DataFrame(columns=["NAME", "LATITUDE", "LONGITUDE", "DISTANCE"])

index_number_list = []
distances_list = []

for i in range(1, 6):
    index_number_list.append(list(sorted_distance_dict.keys())[i])
    distances_list.append(sorted_distance_dict[list(sorted_distance_dict.keys())[i]])

for j in range(len(distances_list)):
    location_stats = location_stats.append({"LATITUDE": df["location.lat"].iloc[index_number_list[j]],
                                            "LONGITUDE": df["location.lng"].iloc[index_number_list[j]],
                                            "NAME": df["name"].iloc[index_number_list[j]],
                                            "DISTANCE": distances_list[j]}, ignore_index=True)

print(location_stats.head())

