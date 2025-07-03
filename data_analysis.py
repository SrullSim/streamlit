import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello World!")
st.write("Hello Streamlit!")

#read in the file
movies_data = pd.read_csv("https://raw.githubusercontent.com/danielgrijalva/movie-stats/7c6a562377ab5c91bb80c405be50a0494ae8e582/movies.csv")


movies_data.duplicated()
movies_data.count()
movies_data.dropna()

st.write("""
Average Movie Budget, Grouped by Genre
""")
avg_budget = movies_data.groupby('genre')['budget'].mean().round()
avg_budget = avg_budget.reset_index()
genre = avg_budget['genre']
avg_bud = avg_budget['budget']


fig = plt.figure(figsize = (19, 10))

plt.bar(genre, avg_bud, color = 'maroon')
plt.xlabel('genre')
plt.ylabel('budget')
plt.title('Matplotlib Bar Chart Showing the Average \
Budget of Movies in Each Genre')

st.pyplot(fig)


# set columns
col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")

scor_rating = movies_data["score"].unique().tolist()
genre_list = movies_data["genre"].unique().tolist()
year_list = movies_data["year"].unique().tolist()

