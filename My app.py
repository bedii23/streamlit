import streamlit as st
import pandas as pd

st.title('Hello, welcome to my application!')

st.write("Have a look to the dataframe cars")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)
st.write(df_voiture)

st.write("Have a look to the line chart of the horse power")
st.line_chart(df_voiture['hp'])


import seaborn as sns
viz_correlation = sns.heatmap(df_voiture.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
st.write("Have a look to the heatmap correlation of our DataFrame")
st.pyplot(viz_correlation.figure)

viz_correlation2 =sns.barplot(data = df_voiture,
			x = "continent",
            y = "hp")
st.write("Have a look to the bar chart of continent & horse power")

st.bar_chart(data = df_voiture, x = "continent", y = "hp")

df_us = df_voiture[df_voiture.continent == ' US.']
df_eu = df_voiture[df_voiture.continent == ' Europe.']
df_jp = df_voiture[df_voiture.continent == ' Japan.']


continent = st.radio(
    "Continent",
    ('US', 'EU', 'Jap'))
if continent == 'US':
    st.write(df_voiture[df_voiture.continent == ' US.'])
elif continent == 'EU':
    st.write(df_voiture[df_voiture.continent == ' Europe.'])
else :
	st.write(df_voiture[df_voiture.continent == ' Japan.'])