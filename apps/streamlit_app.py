import json
import folium
import numpy          as np
import pandas         as pd
import streamlit      as st
import plotly.express as px

from PIL              import Image
from folium           import plugins
from streamlit_folium import folium_static
from pdf_generator2 import *

st.set_page_config(layout='wide') # turns the app scream "wide" <--->
@st.cache(allow_output_mutation=True) # will use cache memory - faster.
def get_data(path):
    data = pd.read_csv(path)

    return data


def hist_plot(data, column, title=''):
    hist = px.histogram(data[column], title=title)
    hist.figure.savefig(f'../images/{column}.png')
    return hist

# get data
path = '../data/df_houses_full_cleanned.csv'
data = get_data(path)

#==========================================
# sidebar
#==========================================

# add a filter
image = Image.open('../images/germany_flag3.png')
st.sidebar.image(image)
st.sidebar.title('Germany Rental Houses App')
st.sidebar.markdown('#### By **Felipe Demenech Vasconcelos** :sunglasses:')
st.sidebar.header('Filters')

# city filters
f_city = st.sidebar.multiselect('Select City', data['city'].unique())
# pets filter
f_pets = st.sidebar.multiselect('Pets Allowence', data['pets'].unique())
# rent price filter
min_ = int(500)
max_ = int(data['montly_rent'].max())
mean_ = int(data['montly_rent'].mean())
f_rent = st.sidebar.slider('Rent Price Range (€)', min_, max_, (2000, 5000))

# display data
data = data.loc[(data['montly_rent'] >= f_rent[0]) & (data['montly_rent'] <= f_rent[1])]

a1, a2, a3 = st.beta_columns((2.6, 6, 0.1))
b1, b2, b3 = st.beta_columns((2.9, 6, 0.1))

# dataframe download button
st.sidebar.subheader('Report Download')
download = st.sidebar.button('Download')
if download:
    pdf_creator(data)

#data.to_csv('')

#======================================
# app page
#======================================

image2 = Image.open('../images/german_house.jpg')

b2.image(image2)
a2.markdown('# **_Rental Houses in Germany_**')
st.title('Data Overview')

# add a "filter description"
if (f_city != []) & (f_pets != []):
    data = data.loc[(data['city'].isin(f_city)) & (data['pets'].isin(f_pets))]
elif (f_city != []) & (f_pets == []):
    data = data.loc[data['city'].isin(f_city)]
elif (f_city == []) & (f_pets != []):
    data = data.loc[data['pets'].isin(f_pets)]
else:
    data = data

# statistic descritive
num_att = data[['size', 'montly_rent', 'deposit_value', 'm2_value']]
mean = pd.DataFrame(num_att.apply(np.mean))
median = pd.DataFrame(num_att.apply(np.median))
std = pd.DataFrame(num_att.apply(np.std))
max_ = pd.DataFrame(num_att.apply(np.max))
min_ = pd.DataFrame(num_att.apply(np.min))

df = pd.concat([max_, min_, mean, median, std], axis = 1).reset_index()
df.columns = ['ATTRIBUTES', 'MAX', 'MIN', 'MEAN', 'MEDIAN', 'STD']
df.set_index('ATTRIBUTES', inplace=True)

# st.dataframe(df1)
st.markdown('## :large_blue_diamond: **Full Selected Dataset**')
data_button = st.checkbox('Display Dataset')
if data_button:
    st.dataframe(data) # display infos in the webbrowsest
st.markdown('## :bar_chart: **Descriptive Caracteristics**')
st.dataframe(df.T)

#=================================================
# HISTOGRAMS
#=================================================
hist_button = st.checkbox('Display Histograms')
e1, e2 = st.beta_columns((1, 1))
e3, e4 = st.beta_columns((1, 1))

if hist_button:
    e1.plotly_chart(hist_plot(data, 'montly_rent', 'MONTLY RENT (€)'), use_container_width=True)
    e2.plotly_chart(hist_plot(data, 'size', 'SIZE (M²)'), use_container_width=True)
    e3.plotly_chart(hist_plot(data, 'deposit_value', 'DEPOSIT VALUE (€)'), use_container_width=True)
    e4.plotly_chart(hist_plot(data, 'pets', 'PETS'), use_container_width=True)

#=================================================
# GRAPHS
#=================================================
st.markdown('## :clipboard: **Rent Prices Distribution (€)**')

st.markdown(f'**Number of Houses: {data.shape[0]}**')
st.markdown(f'**Average Size: {data["size"].mean():.2f}m²**')
st.markdown(f'**Average Rent Price: {data["montly_rent"].mean():.2f}€**')

ax = px.box(data,
            x='city',
            y='montly_rent',
            points='all',
            labels={
                'city': 'City',
                'montly_rent': 'Rent Amount (€)'
            })
st.plotly_chart(ax, use_container_width=True)

#========================================
# maps
#========================================

st.markdown('## :earth_americas: **Rental Houses Map**')
c1, c2 = st.beta_columns((1, 1))

df = data.sample(10)

# 1st map - houses for rent
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


