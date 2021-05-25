import streamlit as st
import pandas as pd
import numpy as np


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
f_city = st.sidebar.multiselect('Select City', data['city'].unique())
f_pets = st.sidebar.multiselect('Pets', data['pets'].unique())

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

# statistic descritive
num_att = data[['size', 'montly_rent', 'deposit_value', 'm2_value']]
mean = pd.DataFrame(num_att.apply(np.mean))
median = pd.DataFrame(num_att.apply(np.median))
std = pd.DataFrame(num_att.apply(np.std))
max_ = pd.DataFrame(num_att.apply(np.max))
min_ = pd.DataFrame(num_att.apply(np.min))

df = pd.concat([max_, min_, mean, median, std], axis = 1).reset_index()
df.columns = ['attributes', 'max_', 'min_', 'mean', 'median', 'std']

st.dataframe(df)
# st.dataframe(df1)
st.dataframe(data) # display infos in the webbrowser