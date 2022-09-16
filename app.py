import streamlit as st
import pickle
import requests
sim = pickle.load(open('sim','rb'))
def posters(id) : 
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=461b48a5dd075f3266a1e812b31d5ee9'.format(id))
     poster = response.json()
     return 'https://image.tmdb.org/t/p/w500/' + poster['poster_path']
def recommend(m) :
     ind = movies_df[movies_df['title'] == m].index[0]
     recom_list = sorted(list(enumerate(sim[ind])),reverse = True,key = lambda x : x[1])[1:6]
     recommended_movies = []
     recommended_posters = []
     for i in recom_list :
          movie_id = movies_df.iloc[i[0]].id
          recommended_movies.append(movies_df.iloc[i[0]].title)
          recommended_posters.append(posters(movie_id))
     return recommended_movies,recommended_posters

movies = pickle.load(open('movies_list','rb'))
movies_df = movies
movies = movies['title'].values
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
     'Which movie you would like to watch',
     movies)

st.write('You selected:', selected_movie_name)
if st.button('Recommend Similar Movies'):
     names,image = recommend(selected_movie_name)
     col1, col2, col3, col4, col5 = st.columns(5)

     with col1:
          st.text(names[0])
          st.image(image[0])

     with col2:
          st.text(names[1])
          st.image(image[1])

     with col3:
          st.text(names[2])
          st.image(image[2])

     with col4:
          st.text(names[3])
          st.image(image[3])

     with col5:
          st.text(names[4])
          st.image(image[4])

