# https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db

import streamlit as st
from PIL import Image 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

penguins_gentoo_df = []
penguins_chinstrap_df = []
penguins_adelie_df = []

def loadCert():
    import os, ssl
    if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
        ssl._create_default_https_context = ssl._create_unverified_context
    
def loadData(species):
    
    with st.spinner(text="Loading palmerpenguins dataset..."):
        if(species == "Gentoo"):
            penguins_gentoo_df = pd.read_csv("https://raw.githubusercontent.com/rupkohli/penguins/main/raw_data/penguin_gentoo_table_220.csv")
            return penguins_gentoo_df
        if(species == "Chinstrap"):
            penguins_chinstrap_df = pd.read_csv("https://raw.githubusercontent.com/rupkohli/penguins/main/raw_data/penguin_chinstrap_table_221.csv")
            return penguins_chinstrap_df
        if(species == "Adelie"):
            penguins_adelie_df = pd.read_csv("https://raw.githubusercontent.com/rupkohli/penguins/main/raw_data/penguin_chinstrap_table_221.csv")
            return penguins_adelie_df
    #st.success('Loading palmerpenguins dataset...Completed!')
    
def visualisation(df):
    st.title('Create Own Visualization')
    st.markdown("Tick the box on the side panel to create your own Visualization.")
    st.sidebar.subheader('Create Own Visualization')
    if st.sidebar.checkbox('Count Plot'):
        st.subheader('Count Plot')
        st.info("If error, please adjust column name on side panel.")
        column_count_plot = st.sidebar.selectbox("Choose a column to plot count. Try Selecting Sex ",df.columns)
        hue_opt = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting Species ",df.columns.insert(0,None))
        
        fig = sns.countplot(x=column_count_plot,data=df,hue=hue_opt)
        st.pyplot()
            
            
    if st.sidebar.checkbox('Histogram | Distplot'):
        st.subheader('Histogram | Distplot')
        st.info("If error, please adjust column name on side panel.")
        # if st.checkbox('Dist plot'):
        column_dist_plot = st.sidebar.selectbox("Optional categorical variables (countplot hue). Try Selecting Body Mass",df.columns)
        fig = sns.distplot(df[column_dist_plot])
        st.pyplot()
            
            
    if st.sidebar.checkbox('Boxplot'):
        st.subheader('Boxplot')
        st.info("If error, please adjust column name on side panel.")
        column_box_plot_X = st.sidebar.selectbox("X (Choose a column). Try Selecting island:",df.columns.insert(0,None))
        column_box_plot_Y = st.sidebar.selectbox("Y (Choose a column - only numerical). Try Selecting Body Mass",df.columns)
        hue_box_opt = st.sidebar.selectbox("Optional categorical variables (boxplot hue)",df.columns.insert(0,None))
        # if st.checkbox('Plot Boxplot'):
        fig = sns.boxplot(x=column_box_plot_X, y=column_box_plot_Y,data=df,palette="Set3")
        st.pyplot()
    return

def describe_species(species):
        st.write("Loading info for species: ", species)
        df = loadData(species) 
    
        #if st.sidebar.checkbox('Basic info'):
        if st.sidebar.checkbox('Dataset Quick Look'):
            st.subheader('Dataset Quick Look:')
            st.write(df.head())

        if st.sidebar.checkbox("Show Columns"):
            st.subheader('Show Columns List')
            all_columns = df.columns.to_list()
            st.write(all_columns)

        if st.sidebar.checkbox('Statistical Description'):
            st.subheader('Statistical Data Descripition')
            st.write(df.describe())

        if st.sidebar.checkbox('Missing Values?'):
            st.subheader('Missing values')
            st.write(df.isnull().sum())
            
        if st.sidebar.checkbox('Graphics'):
            visualisation(df)
            
        return
                
#### MAIN
    
def main():
    loadCert()

    st.title("Meet The Penguins ^_^ :sunglasses:" )

    img=Image.open('images/logo_palmer_Penguins.png')
    st.image(img,width=100)

    st.markdown("The app shows the data for 3 species of Penguins observed on three islands in the Palmer Archipelago, Antarctica. ")
    st.markdown("""Penguin Species \n - Adelie \n - Chinstrap \n - Gentoo; \n """)
    st.markdown("""DataSet: Palmer Penguins data. \n The data were collected and made available by Dr. Kristen Gorman and Palmer Station, Antarctica, LTER""")
    st.markdown("For more details: https://allisonhorst.github.io/palmerpenguins/articles/intro.html")

    

    if st.button("Meet the Palmer Penguins"):
        img2=Image.open('images/penguin.png')
        if img2.mode != 'RGB':
            img = img.convert('RGB')
        st.image(img, width=300, caption="We are Penguins")
        #Ballons
        st.balloons()
        
    
        st.sidebar.markdown("## Side Panel")
        st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")
        st.header("“Now, Explore Yourself the Palmer Penguins”")
      
    # Showing the original raw data
    #if st.checkbox("Show Raw Data", False):
    #    st.subheader('Raw data')
    #    st.write(df)
    
    st.title('Quick  Explore')
    st.sidebar.subheader(' Quick  Explore - Species')
    st.markdown("Tick the box on the side panel to explore the dataset.")
    
    species_gentoo = st.checkbox("Gentoo")

    species_chinstrap = st.checkbox("Chinstrap")

    species_adelie = st.checkbox("Adelie")

    if species_gentoo:
        describe_species("Gentoo")
    if species_chinstrap:
        describe_species("Chinstrap")
    if species_adelie:
        describe_species("Adelie")
    
            
    return



if __name__ == '__main__':
    main()
