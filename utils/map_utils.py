import requests
import os
from dotenv import load_dotenv

load_dotenv()

city_cache = {}
dist_cache = {}
geometry_cache = {}

def get_coordinates(city):

    if city in city_cache:

        return city_cache[city]
    else:

        api_key = os.getenv('API_NINJAS_KEY')
        api_url = f'https://api.api-ninjas.com/v1/city?name={city}'
        headers = {'X-Api-Key': api_key}
        response = requests.get(api_url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            lon = data[0].get('longitude')
            lan = data[0].get('latitude')
            city_cache[city] = lon,lan
        else:
            print('Can`t connect to Api ', response.status_code)
            lon = 0
            lan = 0

        return lon,lan

def dist_calc(departure, destination):
    cache_key = (departure, destination)

    if cache_key in dist_cache:
        return dist_cache[cache_key]
    else:

        lon_start,lat_start = get_coordinates(departure)

        lon_cel,lat_cel = get_coordinates(destination)

        url = f'http://router.project-osrm.org/route/v1/driving/{lon_start},{lat_start};{lon_cel},{lat_cel}?overview=false'

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                distance = round((data['routes'][0]['distance'])/1000,2)
                dist_cache[cache_key] = distance
                return distance
            else:
                print('Can`t connect to Api ', response.status_code)
                return 0

        except requests.exceptions.RequestException as e:
            print(f"Network error in dist_calc: {e}")
            return 0
    
def get_route_geometry(city1, city2):
    cache_key = (city1, city2)

    if cache_key in geometry_cache:
        return geometry_cache[cache_key]
    else:

        lon_start,lat_start = get_coordinates(city1)

        lon_cel,lat_cel = get_coordinates(city2)

        url = f'http://router.project-osrm.org/route/v1/driving/{lon_start},{lat_start};{lon_cel},{lat_cel}?overview=full&geometries=geojson'

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                route = data['routes'][0]['geometry']['coordinates']
                reverse_cords = [[lat,lon] for lon,lat in route]
                geometry_cache[cache_key] = reverse_cords
                return reverse_cords
            else:
                print('Can`t connect to Api ', response.status_code)
                return 0

        except requests.exceptions.RequestException as e:
            print(f"Network error in dist_calc: {e}")
            return 0