import streamlit as st
import streamlit_shadcn_ui as ui
from db.table_creator import create_db
from services.fleet_manager import load_data,load_packages,simulate_routes
from utils.map_generator import generate_maps
import streamlit.components.v1 as components
from data.log_analysis import get_vehicle_route, get_net_profit_per_vehicle, matplotlib_plot, matplotlib_distance_plot, matplotlib_fuel_plot

st.set_page_config(page_title="Automated Fleet Dispatch & Analytics System", layout="wide", initial_sidebar_state="expanded")

# --- Custom CSS for polishing ---
st.markdown("""
<style>
    div[data-testid="stSidebarNav"] {display: none;}
    .reportview-container {background: #f8f9fa;}
</style>
""", unsafe_allow_html=True)

try:
    df_global, fleet_cars_global, packages_global = load_data()
except Exception:
    df_global, fleet_cars_global, packages_global = [], {}, []

st.sidebar.markdown('##  **Automated Fleet Dispatch & Analytics System**')
st.sidebar.markdown('---')
page = st.sidebar.radio("Navigation", 
                        ["Dashboard", "Tracking Center", "Financial Reports"],
                        label_visibility="collapsed")
st.sidebar.markdown('---')

if page == "Dashboard":
    st.title("Fleet Management Dashboard")
    st.markdown("Monitor and control your entire logistics operations from one centralized view.")
    
    total_vehicles = sum(len(cars) for cars in fleet_cars_global.values()) if isinstance(fleet_cars_global, dict) else 0
    total_packages = len(packages_global) if packages_global else 0
    active_regions = len(fleet_cars_global.keys()) if isinstance(fleet_cars_global, dict) else 0
    
    cols = st.columns(3)
    
    with cols[0]:
        with st.container(border=True):
            st.metric(label="Total Vehicles", value=str(total_vehicles))
            st.caption("Deployed in fleet")
            
    with cols[1]:
        with st.container(border=True):
            st.metric(label="Packages for Today", value=str(total_packages))
            st.caption("Number of packages for today")
            
    with cols[2]:
        with st.container(border=True):
            st.metric(label="Active Regions", value=str(active_regions))
            st.caption("Operational sectors")

    st.markdown("<br/>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("## System Configuration")
            st.markdown("Reset the environment to start a fresh delivery scenario.")
            if st.button("Clean & Reset Database", width='stretch', type="secondary"):
                create_db()
                st.success("Database cleaned and loaded with new packages!")
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("## Fleet Operations")
            st.markdown("Dispatch fleet to dynamically deliver assigned packages.")
            if st.button("Run Route Simulation", width='stretch', type="primary"):
                with st.spinner("Vehicles on the road, calculating optimal distances..."):
                    df_live, f_cars, pckgs = load_data()
                    loaded_df = load_packages(df_live, f_cars, pckgs)
                    simulate_routes(loaded_df, f_cars)
                    generate_maps()
                    st.success("Simulation completed successfully!")

if page == "Tracking Center":
    st.title("Real-Time Tracking Center")
    st.markdown("Live location monitoring for deployed vehicles.")
    
    df, fleet_cars, packages = load_data()
    vehicle_names = [car.name for car_list in fleet_cars.values() for car in car_list] if fleet_cars else []
    
    if vehicle_names:
        with st.container(border=True):
            vehicle = st.selectbox("Select Vehicle ID to Track:", vehicle_names)
            map_route = f"utils/map_{vehicle}.html"

            try:
                with open(map_route, 'r', encoding='utf-8') as f:
                    html_map = f.read()
                components.html(html_map, height=600)
            except FileNotFoundError:
                st.warning(f"No active map found for **{vehicle}**. Please run the simulation first.")
    else:
        st.info("No vehicles available in the fleet.")

if page == "Financial Reports":
    st.title("Financial Reports & Analytics")
    st.markdown("Analyze fleet profitability, efficiency, and logistical performance.")
    
    try:
        tab1, tab2 = st.tabs(["Overview & Charts", "Raw Performance Data"])
        
        with tab1:
            st.markdown("### Executive Visual Summary")
            
            with st.container(border=True):
                st.subheader("Net Profit Margin")
                fig_profit = matplotlib_plot()
                st.pyplot(fig_profit)
            
            col1, col2 = st.columns(2)
            with col1:
                with st.container(border=True):
                    st.subheader("Distance Driven (km)")
                    fig_dist = matplotlib_distance_plot()
                    st.pyplot(fig_dist)
                    
            with col2:
                with st.container(border=True):
                    st.subheader("Fuel Consumption (L)")
                    fig_fuel = matplotlib_fuel_plot()
                    st.pyplot(fig_fuel)
                    
        with tab2: 
            with st.container(border=True):
                st.subheader("Vehicle Delivery Routes")
                routes_df = get_vehicle_route()
                st.dataframe(routes_df, width='stretch')
                
            with st.container(border=True):
                st.subheader("Financial Breakdown per Vehicle")
                profit_df = get_net_profit_per_vehicle()
                st.dataframe(profit_df, width='stretch')
            
    except FileNotFoundError:
        st.warning("Analysis not available. Vehicle log files are missing. Please run a simulation first!")