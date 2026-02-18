import math

cities_coordinates = {
    'Warsaw': (0, 0),
    'Cracow': (0, 300),
    'Gdansk': (0, -320),
    'Wroclaw': (-250, 280),
    'Poznan': (-300, 0),
    'Szczecin': (-450, -200),
    'Rzeszow': (200, 320),
    'Bialystok': (180, -150),
    'Lodz': (-120, 100),
    'Katowice': (-50, 280)
}

def get_coordinates(city):
    x = cities_coordinates[city][0]
    y = cities_coordinates[city][1]

    return x,y

def dist_calc(departure, destination):
    x1,y1 = get_coordinates(departure)

    x2,y2 = get_coordinates(destination)

    distance = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))

    return distance