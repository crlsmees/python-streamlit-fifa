import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    layout="centered"
)

if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown('# FIFA23 OFFICIAL DATASET! ⚽️')
st.sidebar.markdown('Developed by Carlos Mees')

btn = st.link_button('Access data on Kaggle', 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    The dataset of football players from 2017 to 2023 provides comprehensive information 
    about professional football players. The dataset contains a wide range of attributes, 
    including player demographics, physical characteristics, game statistics, contract 
    details, and club affiliations.
    
    With **more than 17,000 records**, this dataset offers a valuable resource for football 
    analysts, researchers, and enthusiasts interested in exploring various aspects of the 
    football world, as it allows for the study of player attributes, performance metrics, 
    market evaluation, club analysis, player positioning, and player development over time.
    """
)