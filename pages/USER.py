import pandas as pd
import pymysql
import streamlit as st

st.title("Users")


connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

c.execute("Select * from users")
rows = c.fetchall()

df = pd.DataFrame(rows, columns=['User ID', 'Email',
                  'Name', 'Membership plans'])
st.dataframe(df)
