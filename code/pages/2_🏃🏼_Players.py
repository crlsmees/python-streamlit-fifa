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

df_players = df_data[df_data['Club'] == club]
players = sorted(df_players['Name'].unique(), key=custom_sort)
player = st.sidebar.selectbox("Player", players)

st.sidebar.divider()

st.sidebar.markdown('Developed by Carlos Mees')

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Club:** {player_stats['Club']}")
col2.markdown(f"**Height:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Weight:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Market value', value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label='Weekly salary', value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label='Termination clause', value=f"£ {player_stats['Release Clause(£)']:,}")