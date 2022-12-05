import pandas as pd
import pymysql
import streamlit as st

st.title("Songs In The Playlist")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from playlist_song")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Song ID', 'Playlist ID'])
st.dataframe(df)
