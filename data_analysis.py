import px
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

with st.sidebar:
    st.write("Select a range on the slider (it represents movie score) \
    to view the total number of movies in a genre that falls \
    within that range ")
    # create a slider to hold user scores
new_score_rating = st.slider(label="Choose a value:",
                             min_value=1.0,
                             max_value=10.0,
                             value=(4.0, 5.0))

new_genre_list = st.multiselect('Choose Genre:',
                                        genre_list, default = ['Animation',
                                         'Horror',  'Fantasy', 'Romance'])

year = st.selectbox('Choose a Year',
    year_list, 0)

score_info = (movies_data['score'].between(*new_score_rating))

#Filter the selectbox and multiselect widget for interactivity
new_genre_year = (movies_data['genre'].isin(new_genre_list)) \
& (movies_data['year'] == year)


col1, col2 = st.columns([2,3])
with col1:
    st.write("""#### Lists of movies filtered by year and Genre """)
    dataframe_genre_year = movies_data[new_genre_year]\
    .groupby(['name',  'genre'])['year'].sum()
    dataframe_genre_year = dataframe_genre_year.reset_index()
    st.dataframe(dataframe_genre_year, width = 400)

with col2:
    st.write("""#### User score of movies and their genre """)
    rating_count_year = movies_data[score_info]\
    .groupby('genre')['score'].count()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'genre', y = 'score')
    st.plotly_chart(figpx)