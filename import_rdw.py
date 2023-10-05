import requests

# specify the brand
selected_brand = input("🚗 Insert a brand:\n")

# uppercase the inserted brand
selected_brand_upper = selected_brand.upper()

# specify the endpoint of the API
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand_upper}"

# execute the request
response = requests.get(endpoint)


# get the data
data = response.json()

# show the first 5 cars
print(data[:5])
pass