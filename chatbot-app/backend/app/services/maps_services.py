# import requests
# from config import MAPPLS_API_KEY

# def get_location_info(place):
#     url = f"https://atlas.mappls.com/api/places/textsearch/json"
#     headers = {"Authorization": f"bearer {MAPPLS_API_KEY}"}
#     params = {"query": place}

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         if "suggestedLocations" in data and len(data["suggestedLocations"]) > 0:
#             loc = data["suggestedLocations"][0]
#             return f"{place} is located at Latitude: {loc['latitude']}, Longitude: {loc['longitude']}."
#     return None
