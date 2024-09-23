import streamlit as st
import pandas as pd

st.title('KingHB')

st.info('App to build Machine Learning models')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
