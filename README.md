# Recommendation_Engine
Movie Recommendation Engine using Collaborative Filtering 


There are 2 folders:
-> ML Model
-> WebApp

# Dataset
MovieLens 100K Dataset
MovieLens data sets were collected by the GroupLens Research Project
at the University of Minnesota.

This data set consists of:
* 100,000 ratings (1-5) from 943 users on 1682 movies.
* Each user has rated at least 20 movies.
* Simple demographic info for the users (age, gender, occupation, zip)

The data was collected through the MovieLens web site
(movielens.umn.edu) during the seven-month period from September 19th,
1997 through April 22nd, 1998. 


# ML Model
Collaborative filtering has been used here. This has been implemeted through Corelation between the user ratings and the movie they rated
Data Analysis has been performed to graphically analyse and visualize the dataset

# Running the Code

The first folder 'ML Model' contains the dataset used and the jupyter notebook which runs the Machine Learning Model
Download the dataset and run the Jupyter notebook

The second Folder 'WebApp' contains a file main.py which is as the name suggests the main file.
In the terminal run the command 'streamlit run main.py' after all the folders and files given are cloned
This will redirect to a locally hosted website on which you can select a movie from the dropdown menu and on clicking Show Recommendations, 5 movies will be recommended to you.
