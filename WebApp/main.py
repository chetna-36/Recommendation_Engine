# importing libraries
import pickle       # python module
import streamlit as st      # framework used
import pandas as pd     # python library
import numpy as np      # python library

# Loading the files generated via Machine Learning model
ratings = pickle.load(open('movie_dict.pkl','rb'))
movie_matrix = pickle.load(open('movie_matrix_dict.pkl','rb'))
df = pickle.load(open('movie_df.pkl','rb'))

# Function to make predictions for the selected movie
def recommend_movie(movie_name):
    movie_user_ratings = movie_matrix[movie_name]
    similar_to_movie = movie_matrix.corrwith(movie_user_ratings)

    corr_movie = pd.DataFrame(similar_to_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)

    corr_movie = corr_movie.join(ratings['num of ratings'])
    predictions = corr_movie[corr_movie['num of ratings'] >= 100].sort_values(by=['Correlation'], ascending=False)

    return predictions.head(5)

# Creating the User Interface
st.header("Movie Recomendation System")
movie_list = df['title'].values
movie_list = np.unique(movie_list)
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",movie_list
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
if(st.button('Show Recommendataion')):
    recommend_movie_names = recommend_movie(selected_movie)
    rm = recommend_movie_names.values
    print(rm)
    for i in range(5):
        st.text(rm[i])
