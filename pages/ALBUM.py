import streamlit as st
import pymysql
import pandas as pd

st.title("ALBUM")

connection = pymysql.connect(
    host="localhost", port=3306, user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from album")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Album ID', 'Number of tracks', 'Album Name',
                  'Artist ID'])
st.dataframe(df)
