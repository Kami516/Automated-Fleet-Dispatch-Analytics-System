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
    return cities_coordinates[city]

def dist_calc(departure, destination):
    lon_start,lat_start = get_coordinates(departure)

    lon_cel,lat_cel = get_coordinates(destination)

    url = f'http://router.project-osrm.org/route/v1/driving/{lon_start},{lat_start};{lon_cel},{lat_cel}?overview=false'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        distance = round((data['routes'][0]['distance'])/1000,2)
    else:
        print('Can`t connect to Api ', response.status_code)
        distance = 0

    return distance