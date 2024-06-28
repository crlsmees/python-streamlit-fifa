import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide"
)

if 'data' not in st.session_state:
    st.session_state['data'] = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)

df_data = st.session_state['data']

def custom_sort(club):
    if club[0].isdigit():
        return (1, club)
    else:
        return (0, club)

clubs = sorted(df_data['Club'].unique(), key=custom_sort)
club = st.sidebar.selectbox("Clubs", clubs)

st.sidebar.divider()

st.sidebar.markdown('Developed by Carlos Mees')

df_filtered = df_data[df_data['Club'] == club].set_index('Name')

st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f'## {club}')

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })