import pandas as pd

def dispatcher(df):
    grouped = df.groupby('region')['weight'].sum().reset_index().sort_values(by='weight', ascending=False)

    return grouped