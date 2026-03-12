import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def get_vehicle_route():
    df = pd.read_csv('data/vehicle_logs.csv')
    df = df.groupby('vehicle')['location'].unique().reset_index()
    df['location'] = df['location'].apply(lambda x: list(x) + ['Warsaw'])

    df = df.rename(columns={'location':'route'})

    return df

def get_net_profit_per_vehicle():
    df = pd.read_csv('data/vehicle_logs.csv')
    result = df[df['action'] == 'return'].copy()
    result['net_profit'] = result['cost_of_package'] - (result['cost_of_fuel'] + result['driver_salary'])

    return result

def get_distance_per_vehicle():
    df = pd.read_csv('data/vehicle_logs.csv')
    df_return = df[df['action'] == 'return'].copy()
    return df_return[['vehicle', 'distance_km']]

def get_fuel_usage_per_vehicle():
    df = pd.read_csv('data/vehicle_logs.csv')
    df_return = df[df['action'] == 'return'].copy()
    df_return = df_return.rename(columns={'fuel_left': 'total_fuel_consumed'})
    return df_return[['vehicle', 'total_fuel_consumed', 'cost_of_fuel']]


def matplotlib_plot():
    sns.set_theme(style="whitegrid", context="talk")
    result = get_net_profit_per_vehicle()

    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=result, 
        x='vehicle', 
        y='net_profit', 
        hue='vehicle',
        legend=False,
        palette="viridis"
    )
    
    for i in ax.containers:
        ax.bar_label(i, padding=3, fmt='%.1f $')
        
    plt.xlabel("")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.ylabel("Net Profit ($)", fontsize=12, fontweight='bold')
    plt.title("Net Profit per Vehicle", fontsize=16, fontweight='bold', pad=15)
    sns.despine(left=True, bottom=True)
    
    plt.tight_layout()
    return fig

def matplotlib_distance_plot():
    sns.set_theme(style="whitegrid", context="talk")
    dist_df = get_distance_per_vehicle()
    
    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=dist_df, 
        x='vehicle', 
        y='distance_km',
        hue='vehicle',
        legend=False,
        palette="rocket"
    )
    
    for i in ax.containers:
        ax.bar_label(i, padding=3, fmt='%.1f km')
        
    plt.xlabel("")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.ylabel("Distance Driven (km)", fontsize=12, fontweight='bold')
    plt.title("Total Distance per Vehicle", fontsize=16, fontweight='bold', pad=15)
    sns.despine(left=True, bottom=True)
    
    plt.tight_layout()
    return fig

def matplotlib_fuel_plot():
    sns.set_theme(style="whitegrid", context="talk")
    fuel_df = get_fuel_usage_per_vehicle()
    
    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(
        data=fuel_df, 
        x='vehicle', 
        y='total_fuel_consumed',
        hue='vehicle',
        legend=False,
        palette="mako"
    )
    
    for i in ax.containers:
        ax.bar_label(i, padding=3, fmt='%.1f L')
        
    plt.xlabel("")
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.ylabel("Fuel Consumed (liters)", fontsize=12, fontweight='bold')
    plt.title("Total Fuel Consumption per Vehicle", fontsize=16, fontweight='bold', pad=15)
    sns.despine(left=True, bottom=True)
    
    plt.tight_layout()
    return fig