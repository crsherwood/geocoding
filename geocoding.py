#!/usr/bin/env python3
# import csv module
import csv

# import free Nominatim geocoder
from geopy.geocoders import Nominatim

# create geolocator
geolocator = Nominatim(user_agent="geocoding")

# csv file to read
filename = "addresses.csv"

# rows in read file
file_rows = []

# open/read from csv file
with open(filename, 'r') as csvfile:
    # create csv reader
    csvreader = csv.reader(csvfile)

    # read and save csv file row to rows array
    for row in csvreader:
        file_rows.append(row)

# create array for geocoded items
geocoded_data = []

# geocode each row
for row in file_rows:
    location = geolocator.geocode(row)
    geocoded_data.append([location.address, location.latitude, location.longitude])

# new csv file
new_filename = "geocoded_addresses.csv"

# new file field names
fields = ['Address', 'Latitude', 'Longitude']

# open/write to csv file
with open(new_filename, 'w') as csvfile:
    # create csv writer
    csvwriter = csv.writer(csvfile)

    # write the headers
    csvwriter.writerow(fields)

    # write data rows
    csvwriter.writerows(geocoded_data)