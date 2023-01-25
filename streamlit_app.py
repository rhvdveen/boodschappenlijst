# main app
import streamlit as st
import pandas
from gsheetsdb import connect

# Create a connection object
conn = connect()


# Perform SQL query on the Google Sheet.
# Uses st.cache to only return when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
  rows = conn.execute(query, headers=1)
  rows = rows.fetchall()
  return rows

st.write("Hello world!")

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query('SELECT * FROM "{sheet_url}"')
#rows2 = run_query(f'SELECT * FROM "{sheet_url}"')
st.dataframe(rows)
#st.dataframe(rows2)
