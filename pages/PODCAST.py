import pandas as pd
import pymysql
import streamlit as st

st.title("Podcasts")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from podcast")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Podcast ID', 'Name', 'Episode Number',
                  'Description', 'Year of Release', 'Length', 'Artist ID'])
df["Length"] = df["Length"].to_string
df = df.loc[:, df.columns != 'Length']
st.dataframe(df)
