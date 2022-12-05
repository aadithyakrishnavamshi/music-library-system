import pandas as pd
import pymysql
import streamlit as st

st.title("Artist")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from artist")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=[
                  'Age', 'Stage name', 'Record Label', 'Artsit ID', 'Description', 'Origin (Country)'])
st.dataframe(df)
