# main app
import streamlit as st
import pandas
from gsheetsdb import connect

# Create a connection object
conn = connect()

""""
grocery_list = []

more_items = True

while more_items:
  grocery_item = input("Wat?")
  grocery_list.append(grocery_item)
  
  keep_adding_items = (input("Meer?")).lower()
  
  if keep_adding_items != 'y':
    more_items = False
 
"""


# Perform SQL query on the Google Sheet.
# Uses st.cache to only return when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
  rows = conn.execute(query, headers=1)
  rows = rows.fetchall()
  return rows

st.title('Boodschappenlijst 2.0')
st.header('Huidige lijst')




# if st.button('Haal lijst op'):
sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')
 # st.dataframe(rows)
for row in rows:
  col1, col2 = st.columns(2)
  with col1:
    st.write(f{row.winkel)
  with col2:
    st.write(f{row.product)

st.write("Hello world!")
