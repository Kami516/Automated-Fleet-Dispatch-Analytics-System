from data.log_analysis import get_vehicle_route
from utils.map_utils import get_coordinates,get_route_geometry
import folium
from folium.plugins import BeautifyIcon
from itertools import pairwise

def generate_maps():
    df = get_vehicle_route()

    for x, route_list in df.iterrows():
        map = folium.Map(location=[52.0, 19.0], zoom_start=6)
        gps_coordinates = []

        for city in route_list['route']:
            lon,lat = get_coordinates(city)
            gps_coordinates.append((lat,lon))
        
        for index,point in enumerate(gps_coordinates,start=0):
            folium.Marker(
                location=point, 
                popup=f'Stop nr {index}',
                icon=BeautifyIcon(
                    icon_shape='marker',
                    number=index,
                    border_color='blue',
                    text_color='red'
                )
            ).add_to(map)

        for city1,city2 in pairwise(route_list['route']):
            detailed_route = get_route_geometry(city1,city2)

            folium.PolyLine(locations=detailed_route, color='blue', weight=4).add_to(map)

        file_path = f"map_{route_list['vehicle']}.html"

        map.save(file_path)
        print(f'Route generated for {route_list['vehicle']}')
