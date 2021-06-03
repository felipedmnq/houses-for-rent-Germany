import json
import time
import base64
import folium
import numpy          as np
import pandas         as pd
import streamlit      as st
import plotly.express as px

from PIL              import Image
from folium           import plugins
from streamlit_folium import folium_static
from pdf_generator import *

today = time.strftime('%d%m%Y-%H%M%S')
st.set_page_config(layout='wide')


@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data


@st.cache(allow_output_mutation=True)
def get_geofile(geo_url):
    geo_json_data = json.load(open(geo_url))
    return geo_json_data


def csv_download_link(data):
    csv = data.to_csv(index=False)
    file_name = f'german_rent_houses_{time}.csv'
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Download CSV file</a>'
    st.sidebar.markdown(href, unsafe_allow_html=True)


def pdf_download_link(pdf):
    #file = pdf_creator(data)
    #pdf_creator(data)
    file_name = f'german_rent_houses_{today}.pdf'
    b64 = base64.b64encode(pdf)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{file_name}">Download PDF file</a>'


def hist_plot(data, column, title=''):
    hist = px.histogram(data[column], title=title)
    hist.figure.savefig(f'../images/{column}.png')
    return hist


def data_overview(data):
    # ==========================================
    # sidebar
    # ==========================================
    # add a filter
    image = Image.open('../images/germany_flag3.png')
    st.sidebar.image(image)
    st.sidebar.title('Germany Rental Houses App')
    st.sidebar.markdown('#### By **Felipe Demenech Vasconcelos** :sunglasses:')
    st.sidebar.markdown('### :mag: Filters')

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

    # csv file download
    st.sidebar.markdown('### :floppy_disk: CSV file Download')
    download_csv = st.sidebar.button('Export to CSV')
    if download_csv:
        csv_download_link((data))

    # pdf report download button
    st.sidebar.markdown('### :floppy_disk: PDF Report Download')
    download = st.sidebar.button('Export to PDF')
    if download:
        html = pdf_download_link(pdf_creator(data).encode("latin-1"))
        st.sidebar.markdown(html, unsafe_allow_html=True)

    # ======================================
    # app page
    # ======================================
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

    df = pd.concat([max_, min_, mean, median, std], axis=1).reset_index()
    df.columns = ['ATTRIBUTES', 'MAX', 'MIN', 'MEAN', 'MEDIAN', 'STD']
    df.set_index('ATTRIBUTES', inplace=True)

    # st.dataframe(df1)
    st.markdown('## :large_blue_diamond: **Full Selected Dataset**')
    data_button = st.checkbox('Display Dataset')
    if data_button:
        st.dataframe(data)  # display infos in the webbrowsest
    st.markdown('## :bar_chart: **Descriptive Caracteristics**')
    st.dataframe(df.T)

    return None


def histogram_plot(data):
    hist_button = st.checkbox('Display Histograms')
    e1, e2 = st.beta_columns((1, 1))
    e3, e4 = st.beta_columns((1, 1))

    if hist_button:
        e1.plotly_chart(hist_plot(data, 'montly_rent', 'MONTLY RENT (€)'), use_container_width=True)
        e2.plotly_chart(hist_plot(data, 'size', 'SIZE (M²)'), use_container_width=True)
        e3.plotly_chart(hist_plot(data, 'deposit_value', 'DEPOSIT VALUE (€)'), use_container_width=True)
        e4.plotly_chart(hist_plot(data, 'pets', 'PETS'), use_container_width=True)

    return None


def sumary_display(data):
    st.markdown('## :clipboard: **Rent Prices Distribution (€)**')

    st.markdown(f'**Number of Houses: {data.shape[0]}**')
    st.markdown(f'**Average Size: {data["size"].mean():.2f}m²**')
    st.markdown(f'**Average Rent Price: {data["montly_rent"].mean():.2f}€**')

    return None

def box_plot_display(data):
    ax = px.box(data,
                x='city',
                y='montly_rent',
                points='all',
                labels={
                    'city': 'City',
                    'montly_rent': 'Rent Amount (€)'
                })
    st.plotly_chart(ax, use_container_width=True)

    return None


def map_display(data):
    st.markdown('## :earth_americas: **Rental Houses Map**')
    c1, c2 = st.beta_columns((1, 1))

    # 1st map - houses for rent
    lat = 51.1642292
    long = 10.4541194

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

    return None


if __name__ == "__main__":
    # get data
    path = '../data/df_houses_full_cleanned.csv'
    data = get_data(path)
    # get geofile
    geo_url = '../data/germany_cities.geo.json'
    geo_json_data = get_geofile(geo_url)
    # data overview
    data_overview(data)
    # histograms
    histogram_plot(data)
    # sumary
    sumary_display(data)
    # boxplot
    box_plot_display(data)
    # maps
    map_display(data)
