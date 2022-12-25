# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# run_query("INSERT INTO mytable VALUES ('Mary', 'dog'), ('John', 'cat'), ('Robert', 'bird');")
x=1
y='namrata'
z='namrata@gmail.com'
p='namr'
q_r="INSERT INTO User_Info VALUES ({ph},'{Nm}','{Em}','{pa_ss}')".format(ph = x, Nm= y, Em= z, pa_ss=p)
conn.commit()
q_r1=q_r
run_query(q_r1)
rows = run_query("SELECT * from User_Info;")
# st.write(rows)
# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

