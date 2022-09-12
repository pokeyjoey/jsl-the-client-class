import requests
response = requests.get("https://data.texas.gov/resource/naix-2893.json?location_name=MAX%27S%20WINE%20DIVE")
restaurant_receipts = response.json()


