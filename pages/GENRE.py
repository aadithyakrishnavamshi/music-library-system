import pandas as pd
import pymysql
import streamlit as st

st.title("Genre")


connection = pymysql.connect(
    host="localhost", port=3306, user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from genre")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['Genre ID', 'Name'])
st.dataframe(df)
