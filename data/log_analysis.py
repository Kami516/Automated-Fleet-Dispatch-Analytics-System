import pandas as pd

def get_vehicle_route():
    df = pd.read_csv('data/vehicle_logs.csv')

    df = df.groupby('vehicle')['location'].unique().reset_index()
    df['location'] = df['location'].apply(lambda x: list(x) + ['Warsaw'])

    df = df.rename(columns={'location':'route'})

    return df