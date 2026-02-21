import sqlite3
import pandas as pd
from models.package import Package

def load_data_from_db():
    conn = sqlite3.connect('logistics_fleet.db')

    df_packages = pd.read_sql_query("SELECT * FROM Packages", conn)
    conn.close()

    df_packages['status'] = df_packages['status'].astype(bool)
    packages = [Package(*row) for row in df_packages.itertuples(index=False)]

    return df_packages,packages