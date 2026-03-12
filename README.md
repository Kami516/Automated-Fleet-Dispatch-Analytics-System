# Logistics Fleet Routing & Analytics Simulator

An interactive Python application built with Streamlit designed to simulate delivery fleet operations, optimize package dispatch, and provide comprehensive financial tracking. This project demonstrates backend logistical architecture paired with a modern, data-driven dashboard interface.

## 🚀 Key Features

- **Route Simulation & Mapping**: Calculates geographical distances and dynamically plots vehicle routes in real-time onto interactive HTML maps using `folium`.
- **Intelligent Dispatch System**: Automatically allocates packages to specific vehicles (Trucks, Vans) across multiple regions based on their volumetric capacity, weight limits, and destination criteria.
- **Financial Analytics Engine**: Tracks operational costs (driver salaries, fuel consumption) versus package delivery revenue to calculate net profit. Generates professional, dark-mode compatible charts via `seaborn` and `matplotlib`.
- **Interactive Dashboard**: A modern UI built with `streamlit` and `streamlit-shadcn-ui`, offering a central hub to start simulations, reset operational databases, track live vehicle routes, and analyze end-of-day financial reports.
- **Data Persistence**: Uses a local SQLite database and CSV logs to persist historical vehicle data, package statuses, and financial metrics across sessions.

## 🛠️ Technology Stack

- **Language**: Python 3.12+ (managed with `uv`)
- **Frontend**: Streamlit, Streamlit-Shadcn-UI, HTML/CSS
- **Data Analysis & Visualization**: Pandas, NumPy, Matplotlib, Seaborn
- **Mapping & Geolocation**: Folium
- **Database**: SQLite3

## 📊 Dashboard Modules

1. **Dashboard Overview**: Macro-level metrics (Total Vehicles, Pending Packages) and operational controls to trigger end-to-end simulations.
2. **Real-Time Tracking Center**: Select a specific vehicle to view its assigned route and exact delivery path on an interactive map.
3. **Financial Reports**: Multi-tab analytics view separating raw performance data tables from executive visual summaries (Profit Margins, Fuel Consumption, Distance Driven).

## ⚙️ Installation & Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Kami516/Automated-Fleet-Dispatch-Analytics-System.git
   cd Automated-Fleet-Dispatch-Analytics-System
   ```

2. **Install dependencies using `uv`:**

   ```bash
   uv sync
   ```

3. **Run the application:**
   ```bash
   uv run streamlit run app.py
   ```

## 📐 Architecture overview

The application follows a structured module pattern:

- `models/`: Contains the core classes (e.g., `Vehicle`, `Package`, `Truck`, `Van`) with their structural capacities and behaviors.
- `services/`: Houses the complex business logic (e.g., `fleet_manager.py`) responsible for grouping, dispatching, and routing.
- `db/`: Handles SQLite schema creation and data loading operations.
- `data/`: Responsible for logging route histories and parsing them via Pandas for reporting.
- `app.py`: The main entry-point serving the Streamlit frontend.
