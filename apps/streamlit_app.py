import streamlit as st
import pandas as pd
import numpy as np
import folium
import json
from folium import plugins
from streamlit_folium import folium_static
from PIL import Image


st.set_page_config(layout='wide') # turns the app scream "wide" <--->
@st.cache(allow_output_mutation=True) # will use cache memory - faster.
def get_data(path):
    data = pd.read_csv(path)

    return data


# get data
path = '../data/df_houses_full_cleanned.csv'
data = get_data(path)

#-------------------
# data overview
#-------------------

# add a filter
#f_attributes = st.sidebar.multiselect('Enter columns', data.columns)

image = Image.open('../images/germany_flag3.png')
st.sidebar.image(image)
st.sidebar.title('Germany Rental Houses App')
st.sidebar.markdown('#### By **Felipe Demenech Vasconcelos** :sunglasses:')
st.sidebar.header('Filters')
f_city = st.sidebar.multiselect('Select City', data['city'].unique())
f_pets = st.sidebar.multiselect('Pets Allowence', data['pets'].unique())

a1, a2, a3 = st.beta_columns((2.6, 6, 0.1))
b1, b2, b3 = st.beta_columns((2.9, 6, 0.1))
#a2.markdown("<h1 style='text-align: center; color: red;'>German Rent Houses</h1>", unsafe_allow_html=True)
image2 = Image.open('../images/german_house.jpg')

b2.image(image2)
a2.markdown('# **_Rental Houses in Germany_**')
st.title('Data Overview')

df1 = data.groupby('city')['size', 'montly_rent', 'deposit_value', 'm2_value'].mean().round(2).reset_index()
df1.columns = ['CITY', 'AVG SIZE', 'AVG RENT PRICE (€)', 'AVG DEPOSIT VALUE (€)', 'AVG M2 PRICE (€)']


# add a "filter description"
if (f_city != []) & (f_pets != []):
    data = data.loc[(data['city'].isin(f_city)) & (data['pets'].isin(f_pets))]
elif (f_city != []) & (f_pets == []):
    data = data.loc[data['city'].isin(f_city)]
elif (f_city == []) & (f_pets != []):
    data = data.loc[data['pets'].isin(f_pets)]
else:
    data = data


#c1, c2 = st.beta_columns((1, 1)) # inputs like columns
# statistic descritive
num_att = data[['size', 'montly_rent', 'deposit_value', 'm2_value']]
mean = pd.DataFrame(num_att.apply(np.mean))
median = pd.DataFrame(num_att.apply(np.median))
std = pd.DataFrame(num_att.apply(np.std))
max_ = pd.DataFrame(num_att.apply(np.max))
min_ = pd.DataFrame(num_att.apply(np.min))

df = pd.concat([max_, min_, mean, median, std], axis = 1).reset_index()
df.columns = ['attributes', 'max_', 'min_', 'mean', 'median', 'std']


# st.dataframe(df1)
st.header('Dataset')
st.dataframe(data) # display infos in the webbrowsest
st.header('Descriptive Caracteristics')
st.dataframe(df)

#-------------------
# maps
#-------------------

st.markdown('## :earth_americas: Rental Houses Map')
c1, c2 = st.beta_columns((1, 1))

#c1.header('Map - 01')
df = data.sample(10)

# base map
lat = 51.1642292
long = 10.4541194

germany = '../data/germany_cities.geo.json'
geo_json_data = json.load(open(germany))

map_b = folium.Map(location=[lat, long], zoom_start=5.5)

prices = plugins.MarkerCluster().add_to(map_b)

for lat, lng, i in zip(data['lat'],
                       data['long'],
                       list(range(data.shape[0]))):
    label = f'{data["street"].values[i]} - Price: €{data["montly_rent"].values[i]} - {data["pets"].values[i]}'
    label = folium.Popup(label, parse_html=True)
    folium.Marker(
        location=[lat, lng],
        icon=None,
        popup=label).add_to(prices)

folium.GeoJson(geo_json_data, style_function=lambda feature: {'color': 'darkred', 'weight': 0.5, }).add_to(map_b)

folium_static(map_b, width=1200, height=550)



