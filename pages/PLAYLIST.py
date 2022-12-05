import pandas as pd
import pymysql
import streamlit as st

st.title("Playlist")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from playlist")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Playlist ID', 'Name',
                  'Number of tracks', 'Description', 'Genre ID'])
st.dataframe(df)
