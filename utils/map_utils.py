import requests

def get_coordinates(city):
    api_key = 'yKIeo0IoSHEBdFCpO7bQBVfwyqGOiuHp0YgRmQon'
    api_url = f'https://api.api-ninjas.com/v1/city?name={city}'
    headers = {'X-Api-Key': api_key}
    response = requests.get(api_url, headers)

    if response.status_code == 200:
        data = response.json()
        lon = data[0].get('longitude')
        lan = data[0].get('latitude')
    else:
        print('Can`t connect to Api ', response.status_code)
        lon = 0
        lan = 0
        
    return lon,lan

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