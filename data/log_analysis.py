import pandas as pd

df = pd.read_csv('data/vehicle_logs.csv')

def get_vehicle_route():

    df = df.groupby('vehicle')['location'].unique().reset_index()
    df['location'] = df['location'].apply(lambda x: list(x) + ['Warsaw'])

    df = df.rename(columns={'location':'route'})

    return df

def get_net_profit_per_vehicle():
    result = df[df['action'] == 'return']
    result['net_profit'] = result['cost_of_package'] - (result['cost_of_fuel'] + result['driver_salary'])

    return result