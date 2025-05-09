import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

print("Current directory:", os.getcwd())

# Load ratings and movie titles
ratings = pd.read_csv('u.data', sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])
movies = pd.read_csv('u.item', sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=['movieId', 'title'])

# Merge and create matrix
data = pd.merge(ratings, movies, on='movieId')
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating').fillna(0)

# Compute cosine similarity
similarity = cosine_similarity(user_movie_matrix.T)
sim_df = pd.DataFrame(similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Recommend
def get_similar_movies(movie, n=5):
    if movie not in sim_df.columns:
        return "Movie not found."
    return sim_df[movie].sort_values(ascending=False)[1:n+1]

print(get_similar_movies("Star Wars (1977)"))
