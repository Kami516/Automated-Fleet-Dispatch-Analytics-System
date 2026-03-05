from services.fleet_manager import load_data,load_packages,simulate_routes
from db.table_creator import create_db
from utils.map_generator import generate_maps
from utils.map_utils import get_route_geometry
from data.log_analysis import get_net_profit_per_vehicle

def manager():
    create_db()
    df, fleet_cars,packages = load_data()
    loaded_df = load_packages(df, fleet_cars,packages)
    simulate_routes(loaded_df, fleet_cars)

def main():
    print("Hello from logistics-fleet-simulator!")
    manager()
    #generate_maps()
    df = get_net_profit_per_vehicle()
    print(df)

if __name__ == "__main__":
    main()
