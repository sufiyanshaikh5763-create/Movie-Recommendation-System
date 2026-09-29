## Importing Libraries
import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")
## Accesing the required files
with open('movies.pickle','rb') as m:
    movies=pickle.load(m)

similarity=joblib.load("similarity.joblib")

movies_names=movies['title'].values

## Recommend function
def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]
    recommendations=similarity[movie_index]
    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movie=[]

    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

name_movie=st.selectbox("Enter the movie name",movies_names)


if st.button("Recommend"):
    r=recommend(name_movie)

    st.write("The Recommended movies are:")
    for i in r:
        st.write(i)