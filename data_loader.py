import pandas as pd
import numpy as np
import streamlit as st
import pydeck as pdk


@st.cache(persist=True)
def load_location_data():
    data = pd.read_csv('./data/BC_Lightstations_and_other_Sample_Sites.csv', skiprows=1)
    data.rename(columns={
        'LATITUDE (DECIMAL DEGREES)': 'latitude',
        'Unnamed: 4': 'longitude',
        'LIGHTSTATION / LOCATION': 'lightstation'
    }, inplace=True)
    data.rename(str.lower, axis='columns', inplace=True)
    return data

def load_farm_data():
    # Fish farm data
    data = pd.read_csv('./data/lice-count-dens-pou-2011-ongoing-rpt-pac-dfo-mpo-aquaculture-eng.csv')
    data.columns
    data.rename(columns = {
        'Latitude (Decimal Degrees)': 'latitude',
        'Longitude (Decimal Degrees)': 'longitude',
        'Facility Reference \nNumber': 'facility'
    }, inplace=True)
    data.rename(str.lower, axis='columns', inplace=True)
    return data

ls_data = load_location_data()
st.header("Active station locations")

active = ls_data[ls_data['data collection status']=='ACTIVE']
inactive = ls_data[ls_data['data collection status']!='ACTIVE']

st.map(active[['longitude', 'latitude']])

ff_data = load_farm_data()
farms = ff_data[['facility', 'latitude', 'longitude']]
farms = farms.drop_duplicates(subset=['facility'])
st.header("Farm locations")
st.map(farms[['longitude', 'latitude']])
