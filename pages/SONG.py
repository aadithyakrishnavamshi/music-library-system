import pandas as pd
import pymysql
import streamlit as st

st.title("Tracks")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from song")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Song ID', 'Name', 'Year of release', 'Record label',
                  'Language', 'Length', 'Artist ID', 'Album ID'])
df["Length"] = df["Length"].to_string
# df.drop(["Length"])
df = df.loc[:, df.columns != 'Length']


st.dataframe(df)
