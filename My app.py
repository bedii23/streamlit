import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Ici je configure ma page
st.set_page_config(
    page_title="App of DataFrame cars",
    page_icon="🚗")

# Ici je précise mon titre
st.title('Hello, voilà mon application!')
# Ici le sous titre
st.header("Jétons un oeil au dataframe 'cars'")
# Mon DataFrame
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
# Ici je configure ma barre latérale
st.sidebar.image("accueil.jpg")
continent = st.sidebar.radio("Continent :", ('Tous','US', 'EU', 'Jap'))
genre = st.sidebar.radio("Catégorie :",df_cars.columns.values)
# Ici je configure mes 3 différentes tabulations
tab1, tab2, tab3 = st.tabs(["Data Frame", "Correlation", "Distribution"])
# Je commence par la 1ère tab et j'y insère ce dont je veux afficher et ainsi de suite
with tab1:
    if continent == 'Tous':
        df_auto = df_cars
        df_auto
    elif continent == 'US':
        df_auto = df_cars.loc[(df_cars["continent"] == " US.")]
        df_auto
    elif continent == 'EU':
        df_auto = df_cars.loc[(df_cars['continent'] == " Europe.")]
        df_auto
    elif continent == 'Jap':
        df_auto = df_cars.loc[(df_cars['continent'] == " Japan.")]
        df_auto


with tab2:
    fig, ax = plt.subplots(figsize=(8, 8))
    ax = sns.set_theme(style="whitegrid")

    ax = sns.heatmap(df_auto.corr(), 
        center=0,
        cmap=sns.color_palette("vlag", as_cmap=True),
        vmin=-1,
        vmax=1,
        square=True,                
        linewidths=5,               
        cbar_kws={"shrink": .6},                                
        linecolor='white')

    if continent == 'Tous':
        st.write("De manère générale nous pouvons nous apercevoir et pour chaque continent qu'il y a des fortes corrélations positives entre les catégories cylinder, cubicinches, hp et weightlbs.")
    elif continent == 'US':
        st.write("La tendance générale est toujours présente concernant les corrélations positives. On remarque aussi qu'il y a des fortes corrélation négatives entre les catégories mpg, cylinder, cubicinches, hp, weightlbs et enfin time-to-60.")
    elif continent == 'EU':
        st.write("La tendance générale est toujours présente concernant les corrélations positives. Il y a aussi quelques corrélations négatives notamment entre les catégories mpg, cubicinches, hp, weightlbs et time-to-60. De plus on remarque aussi qu'il y a des corrélations nulles entre les catégories time-to-60, cylinder, cubicinches, weightlbs, year et hp.")
    elif continent == 'Jap':
        st.write("La tendance générale est toujours présente concernant les corrélations positives. Il y a aussi quelques corrélations négatives notamment entre les catégories mpg, cubicinches, hp, weightlbs et time-to-60. De plus on remarque aussi qu'il y a des corrélations nulles entre les catégories year, time-to-60, cylinder.")

    fig = plt.title('Corrélation entre les différentes charactéristiques des voitures', size = 15)

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()
    
    st.header("Ci-dessous le tableau de corrélation avec les valeurs")
    st.dataframe(df_auto.corr())


with tab3:
    fig, viz_distri = plt.subplots(figsize=(6, 6))
    viz_distri = sns.displot(df_auto, x=genre, hue="continent", element="step", discrete= False)
    fig = plt.title('Distribution entre les différentes charactéristiques des voitures', size = 15)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()