import requests
import sys
import os

# specify the brand
selected_brand = input("🚗 Insert a brand:\n")

# uppercase the inserted brand
selected_brand_upper = selected_brand.upper()

# specify the endpoint of the API
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

# execute the request
response = requests.get(endpoint)

# check if the response code is 200
if not response.status_code == 200:
    print("Something went wrong")
    print(f"{response.status_code}")
    sys.exit()

# get the data
data = response.json()

# check if the list is empty
if len(data) == 0:
    print(f"No cars found for the brand {selected_brand}")
    sys.exit()

# show the first 5 cars
print(data[:5])

# create the folder for this brand if it does not exist alrady
files_folders = os.listdir()

# check if the folder already exists
if selected_brand_upper not in files_folders:
    print(f"📂 Creating folder '{selected_brand_upper}'")
    os.mkdir(selected_brand_upper)



pass