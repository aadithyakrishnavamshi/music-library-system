import streamlit as st
import pandas as pd
import pymysql

st.title("Music Library System")
st.subheader("PES2UG20CS003")
connection = pymysql.connect(host="localhost", port=3306,
                             user="root", passwd="", database="music_library")
c = connection.cursor()

with st.form("q_box"):
    q = st.text_input("Enter Query: ")

    submitted = st.form_submit_button("Submit")

    if submitted:
        c.execute(q)
        rows = c.fetchall()
        df = pd.DataFrame(rows)
        st.dataframe(df)
        df.iloc[0:0]
connection.close()
