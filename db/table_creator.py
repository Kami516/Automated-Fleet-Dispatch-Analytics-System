import sqlite3

def create_tables():
    script =(
        '''DROP TABLE IF EXISTS Packages;
        CREATE TABLE IF NOT EXISTS Packages(
        id INTEGER PRIMARY KEY,
        weight INTEGER,
        destination TEXT,
        region TEXT,
        status INTEGER
        );

        DROP TABLE IF EXISTS Vehicles;
        CREATE TABLE IF NOT EXISTS Vehicles(
        id INTEGER PRIMARY KEY,
        name TEXT,
        position TEXT,
        max_load INTEGER,
        fuel_max INTEGER,
        fuel_consumption INTEGER,
        region TEXT,
        type TEXT
        );
        '''
    )

    return script

def insert_packages():

    data = [
        # North
        (11, 350, 'Gdansk', 'North', 0),
        (12, 120, 'Gdansk', 'North', 0),
        (13, 15, 'Szczecin', 'North', 0),
        (14, 200, 'Szczecin', 'North', 0),
        (29, 85, 'Bialystok', 'North', 0),
        (30, 10, 'Bialystok', 'North', 0),
        # South
        (15, 400, 'Katowice', 'South', 0),
        (16, 50, 'Katowice', 'South', 0),
        (17, 75, 'Krakow', 'South', 0),
        (18, 5, 'Rzeszow', 'South', 0),
        (19, 180, 'Rzeszow', 'South', 0),
        # West
        (25, 140, 'Poznan', 'West', 0),
        (26, 60, 'Poznan', 'West', 0),
        (27, 300, 'Wroclaw', 'West', 0),
        (28, 45, 'Wroclaw', 'West', 0),
        # Center
        (23, 250, 'Lodz', 'Center', 0),
        (24, 20, 'Lodz', 'Center', 0)
    ]

    script = (
        '''INSERT INTO Packages(id,weight,destination,region,status) VALUES (?,?,?,?,?);
        '''
    )

    return script,data

def create_db():
    create_packages_script = create_tables()
    insert_packages_script,data = insert_packages()

    with sqlite3.connect('logistics_fleet.db') as conn:
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.executescript(create_packages_script)
        print('Data Base created succesfully')
        cur.executemany(insert_packages_script,data)
        conn.commit()
        print(f'Added {len(data)} packages into data base!')