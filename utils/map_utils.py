import math
import requests

cities_coordinates = {
    'Warsaw': (21.0122, 52.2297),
    'Gdansk': (18.6466, 54.3520),
    'Szczecin': (14.5528, 53.4285),
    'Bialystok': (23.1688, 53.1325),
    'Katowice': (19.0238, 50.2649),
    'Cracow': (19.9450, 50.0647),
    'Rzeszow': (21.9990, 50.0412),
    'Poznan': (16.9252, 52.4064),
    'Wroclaw': (17.0385, 51.1079),
    'Lodz': (19.4570, 51.7592)
}

def get_coordinates(city):
    x = cities_coordinates[city][0]
    y = cities_coordinates[city][1]

    return x,y

def dist_calc(departure, destination):
    lon_start,lat_start = get_coordinates(departure)

    lon_cel,lat_cel = get_coordinates(destination)

    url = f'http://router.project-osrm.org/route/v1/driving/{lon_start},{lat_start};{lon_cel},{lat_cel}?overview=false'

    request = requests.get(url)
    response = request.json()

    distance = round((response['routes'][0]['distance'])/1000,2)

    return distance