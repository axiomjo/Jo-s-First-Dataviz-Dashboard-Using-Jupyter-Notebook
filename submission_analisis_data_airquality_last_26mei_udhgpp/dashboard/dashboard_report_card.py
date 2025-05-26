import streamlit as st
import pandas as pd
import math
from pathlib import Path


import matplotlib.pyplot as mpl
import matplotlib.colors as mcolors
import seaborn as sb

import numpy as np
import pandas as pd

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='2013-2017 Beijing PRSA stations: city & pollutant overview',
    page_icon=':toolbox:', # This is an emoji shortcode. Could be a URL too.
)

# Set the title that appears at the top of the page.
'''
# :toolbox: BEIJING'S POLLUTANT IN DATA (2013-2017)

Look around and play with the dataviz-es of Beijing Municipal Environmental Monitoring Center 's air quality data! 
'''

'''
**DATA SOURCE**:  
The data is from aaaaa
https://www.kaggle.com/datasets/sid321axn/beijing-multisite-airquality-data-set,
and i discovered it from Dicoding's "Belajar Analisis Data dengan Python" course :>

'''

# Add some spacing
''
''

#========================== perkara NGIMPOR DATA BUAT DATAVIZ ==========================

@st.cache_data
def load_data():
    df = pd.read_csv('submission-dicoding-analisis-data/data/FULL_DATA_BUAT_DASHBOARD.csv')
    return df

# Load data (cached)
cleaned_data_semua_area = load_data()



# Get unique stations
key_stasiun_data = cleaned_data_semua_area["station"].unique()
key_polutan_data = ["CO","NO2","O3", "PM10", "PM2.5", "SO2" ]



#========================== perkara color pallete ==========================



# 🎨 Generate Unique Colors for Stations
station_colors = [mcolors.to_hex(c) for c in mpl.cm.viridis(np.linspace(0, 1, len(key_stasiun_data)))]
station_color_map = dict(zip(key_stasiun_data, station_colors))

# 🎨 Generate Unique Colors for Pollutants (Using Plasma Palette)
pollutant_colors = [mcolors.to_hex(c) for c in mpl.cm.plasma(np.linspace(0, 1, len(key_polutan_data)))]
pollutant_color_map = dict(zip(key_polutan_data, pollutant_colors))

# 🎨 color pallete buat standar WHO
palet_jojo = ["#A6D75B", "#E07A5F", "#D07666", "#B85042", "#7A3E2F", "#332D2D"]
bin_labels = [
    "1: di bawah AQG",
    "2: di bawah IT4",
    "3: di bawah IT3",
    "4: di bawah IT2",
    "5: di bawah IT1",
    "6: di atas IT1"
]

#========================== perkara bikin dataframe buat grafik ==========================





#============================== perkara tabs per polutan ==========================
tabs = st.tabs(key_polutan_data)

for tab, tiap_polutan in zip(tabs, key_polutan_data):
    with tab:
        st.subheader(f"bla{tiap_polutan}")
        


#----------------------------
'''
NTAR BALIKIN Y JO.
'''
# Display Color Palette as Markdown
# tab2.subheader("🎨 Pollutant Colors")
# for pollutant, color in pollutant_color_map.items():
#     tab2.markdown(f"<span style='background-color:{color}; padding:5px 10px; border-radius:5px; color:white'>{pollutant}</span>", unsafe_allow_html=True)


# tab2.subheader("🎨 Station Colors")
# for station, color in station_color_map.items():
#     tab2.markdown(f"<span style='background-color:{color}; padding:5px 10px; border-radius:5px; color:white'>{station}</span>", unsafe_allow_html=True)

#----------------------------
tabs = st.tabs(cities)




#========================== perkara settings sidebar==========================
st.sidebar.title("🔧 Dashboard Settings")

st.sidebar.markdown(
    """
    This is a simple dashboard to visualize GDP data from 1960 to 2022.
    You can select the year and country you want to see.
    
    | kriteria  | warna  |
|-----------|-----------|
|  **0**< x < AQG Level      |<span style="background-color: #A6D75B; color: #000;">A6D75B</span> |
| **AQG Level** < x < Interim Target 4       | <span style="background-color: #E07A5F; color: #000;">E07A5F</span>    |
| **Interim Target 4** < x <Interim Target 3    | <span style="background-color: #D07666; color: #000;">D07666</span>  |
| **Interim Target 3** < x <Interim Target 2    | <span style="background-color: #B85042; color: #000;">B85042</span>   |
| **Interim Target 2** < x <Interim Target 1   | <span style="background-color: #7A3E2F; color: #000;">7A3E2F</span>  |
| **Interim Target 1** < x   | <span style="background-color: #332D2D; color: #000;">332D2D</span>  |
    
    """
)

#======== checkbox polutan
st.sidebar.subheader("POLLUTANTS")

polutan_checkbox_states = {}
for tiap_polutan in key_polutan_data:
    col1, col2 = st.sidebar.columns([0.7, 0.3])  

    with col1:
        checked = st.checkbox(tiap_polutan, value=True, key=f"st_{tiap_polutan}")
    with col2:
        if checked:
            temp_warna= pollutant_color_map[tiap_polutan]
        else:
            temp_warna= "#D3D3D3"
        
        
        st.markdown(f"<div style='width: 40px; height: 20px; background-color:{temp_warna}; border-radius:3px'></div>", unsafe_allow_html=True)

    polutan_checkbox_states[tiap_polutan] = checked  

selected_polutant = [pollutant for pollutant, checked in polutan_checkbox_states.items() if checked]
st.sidebar.write(f"polutan yg kepilih: {', '.join(selected_polutant)}")




st.sidebar.markdown(
    """
      

    """
)


#======== checkbox stasiun
st.sidebar.subheader("STATIONS")

stasiun_checkbox_states = {}
for tiap_stasiun in key_stasiun_data:
    col1, col2 = st.sidebar.columns([0.7, 0.3])  

    with col1:
        checked = st.checkbox(tiap_stasiun, value=True, key=f"st_{tiap_stasiun}")
    with col2:
        if checked:
            temp_warna= station_color_map[tiap_stasiun]
        else:
            temp_warna= "#D3D3D3"
        
        st.markdown(f"<div style='width: 40px; height: 20px; background-color:{temp_warna}; border-radius:3px'></div>", unsafe_allow_html=True)

    stasiun_checkbox_states[tiap_stasiun] = checked  

selected_stations = [station for station, checked in stasiun_checkbox_states.items() if checked]
st.sidebar.write(f"stasiun yg kepilih: {', '.join(selected_stations)}")






#=============== polarplot stasiun per polutan

import numpy as np
import matplotlib.pyplot as plt

# 🎯 Pre-filter data once instead of inside the loop
filtered_data = cleaned_data_semua_area[cleaned_data_semua_area["station"].isin(selected_stations)]

# 🎯 Precompute monthly averages for all stations & pollutants
monthly_avg = filtered_data.groupby(["month", "station"])[selected_polutant].mean().unstack(level=1)

# 🎯 Convert month index to radians
theta = (monthly_avg.index - 1) * (2 * np.pi / 12)

# 🎨 Create subplots (2 rows x 3 cols) with polar projection
fig, axes = plt.subplots(nrows=2, ncols=3, subplot_kw={'projection': 'polar'}, figsize=(15, 10))
axes = axes.flatten()

# 🎯 Loop through each pollutant
for i, tiap_polutan in enumerate(selected_polutant):
    ax = axes[i]

    # 🎯 Loop through stations, but now using precomputed `monthly_avg`
    for tiap_stasiun in selected_stations:
        values = monthly_avg[tiap_polutan][tiap_stasiun].values  # Precomputed mean values
        
        # Close the cycle (repeat January at the end)
        theta_closed = np.append(theta, 2 * np.pi)
        values_closed = np.append(values, values[0])

        # 🎨 Plot the data
        ax.plot(theta_closed, values_closed, label=tiap_stasiun, 
                color=station_color_map[tiap_stasiun], alpha=0.7)

    # 📌 Format plot
    ax.set_title(tiap_polutan, fontsize=12)
    ax.set_xticks(np.linspace(0, 2 * np.pi, 12, endpoint=False))  # 12 evenly spaced ticks
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.legend(fontsize=7, loc="upper left")

# 🌍 Title and layout
plt.suptitle("Siklus Tahunan Konsentrasi Polutan", fontsize=16)
st.pyplot(fig)



#=============== scatterplot stasiun per polutan

cleaned_data_semua_area["timestamp"] = pd.to_datetime(cleaned_data_semua_area["timestamp"])

# Filter data based on selected stations
temp_scatterplot_stasiun_data = cleaned_data_semua_area[cleaned_data_semua_area["station"].isin(selected_stations)]

st.title("📊 Air Quality Dashboard")

# Check if any station is selected
if selected_stations:
    # Create subplots
    fig, axes = mpl.subplots(nrows=len(selected_polutant), ncols=1, figsize=(18, 30))
    axes = axes.flatten()

    for i, polutan in enumerate(selected_polutant):
        ax = axes[i]

        # Filter and process data
        temp_df = temp_scatterplot_stasiun_data[["timestamp", "station", polutan]].copy()
        temp_df["date"] = temp_df["timestamp"].dt.date  # Extract only date
        temp_df = temp_df.groupby(["date", "station"])[polutan].mean().reset_index()

        # Scatter plot
        sb.scatterplot(
            data=temp_df,
            x="date",
            y=polutan,
            hue="station",
            alpha=0.6,
            palette=station_color_map,
            ax=ax
        )

        ax.set_title(f"Konsentrasi {polutan}", fontsize=12)
        ax.set_ylabel(polutan)
        ax.legend(loc="upper right", fontsize=8)
        ax.tick_params(axis="x", rotation=45)

    mpl.tight_layout()
    st.pyplot(fig)
else:
    st.warning("⚠️ kok gaada stasiun yg dipilih? :c")


