from services.fleet_manager import load_data,load_packages,simulate_routes

def manager():
    df, fleet_cars,packages = load_data()
    loaded_df = load_packages(df, fleet_cars,packages)
    simulate_routes(loaded_df, fleet_cars)

def main():
    print("Hello from logistics-fleet-simulator!")
    manager()


if __name__ == "__main__":
    main()
