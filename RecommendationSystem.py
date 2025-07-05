import numpy as np

ratings = np.array([
    [4, 0, 0, 5, 1, 1, 0],
    [5, 5, 4, 0, 1, 0, 1],
    [0, 0, 0, 2, 3, 5, 0],
    [3, 0, 0, 0, 0, 1, 3],
])

def cosine_similarity(matrix):
    """Compute the cosine similarity between rows of the given matrix."""
    similarity = np.dot(matrix, matrix.T)
    norms = np.array([np.sqrt(np.diagonal(similarity))])
    return (similarity / norms / norms.T)

def predict_ratings(ratings, similarity, user_index):
    """Predict the ratings for a given user based on item similarity."""
    user_ratings = ratings[user_index]
    weighted_sum = np.dot(similarity[user_index], ratings)
    sum_of_weights = np.array([np.abs(similarity[user_index]).sum(axis=0)])
    predicted_ratings = weighted_sum / sum_of_weights
    return np.nan_to_num(predicted_ratings)

def recommend(ratings, user_index, top_n=3):
    """Recommend items to the given user."""
    similarity = cosine_similarity(ratings)
    predicted_ratings = predict_ratings(ratings, similarity, user_index)
    unrated_indices = np.where(ratings[user_index] == 0)[0]
    recommendations = sorted(
        [(index, predicted_ratings[index]) for index in unrated_indices],
        key=lambda x: -x[1]
    )
    return recommendations[:top_n]

user_index = 0
recommendations = recommend(ratings, user_index)
print("Recommendations for user 0:")
for movie_index, predicted_rating in recommendations:
    print(f"Movie {movie_index}: Predicted Rating {predicted_rating:.2f}")