import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def get_vehicle_route():
    df = pd.read_csv('data/vehicle_logs.csv')
    df = df.groupby('vehicle')['location'].unique().reset_index()
    df['location'] = df['location'].apply(lambda x: list(x) + ['Warsaw'])

    df = df.rename(columns={'location':'route'})

    return df

def get_net_profit_per_vehicle():
    result = df[df['action'] == 'return'].copy()
    result['net_profit'] = result['cost_of_package'] - (result['cost_of_fuel'] + result['driver_salary'])

    return result

def matplotlib_plot():
    df = pd.read_csv('data/vehicle_logs.csv')
    result = get_net_profit_per_vehicle()

    plt.bar(result['vehicle'], result['net_profit'])
    plt.xlabel("Vehicle name")
    plt.xticks(rotation=15)
    plt.ylabel("Net Profit")
    plt.title("Net profit per vehicle")
    plt.tight_layout()
    plt.savefig('net-profit.png')
    plt.close()