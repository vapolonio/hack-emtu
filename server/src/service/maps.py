import googlemaps
from datetime import datetime
from settings.constants import API_KEY_MAPS

gmaps = googlemaps.Client(key=API_KEY_MAPS)

def search_direction(origem, destino):
    now = datetime.now()
    directions_result = gmaps.directions(origem,
                                     destino,
                                     mode="transit",
                                     transit_mode="bus",
                                     departure_time=now)
