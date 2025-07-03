import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello World!")
st.write("Hello Streamlit!")

#read in the file
movies_data = pd.read_csv("https://raw.githubusercontent.com/danielgrijalva/movie-stats/7c6a562377ab5c91bb80c405be50a0494ae8e582/movies.csv")

st.write(movies_data)

movies_data.duplicated()
movies_data.count()