import streamlit as st
import pandas as pd

st.title('KingHB')

st.info('App to build Machine Learning models')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
  
  st.write('**X data**')
  x = df.drop('species',axis = 1)
  x
  
  st.write('**Y data**')
  y = df['species']
  y

with st.expander('Data visualization'):
  st.write('**scatter**')
  st.scatter_hart(data = df, x = 'bill_length_mm' ,y = 'body_mass_g',color = 'species')
  
