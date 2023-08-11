import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


file_path = '../data/user_general.json'
with open(file_path, 'r') as file:
    user_data = json.load(file)

#----------------------- dummy data loading ----------------------------

    
# Load the trained model
model = Word2Vec.load("general_model.bin")

# Calculate average vector for user preferences with weighted selected and opposite preferences
def calculate_weighted_average_vector(preferences, selected_weight, opposite_weight):
    total_vector = np.zeros(model.vector_size)
    count = 0
    for preference in preferences:
        # print(preference)
        for key, value in preference.items():
            try:
                total_vector += selected_weight * model.wv[value['selected']]
                total_vector += opposite_weight * model.wv[value['opposite']]
                count += 2
            except KeyError:
                pass
    if count == 0:
        return None
    return total_vector / count

# Calculate and print similarity between users
user1 = user_data[0] # me
user2 = user_data[1]

user1_vector = calculate_weighted_average_vector(user1['general_preference'], selected_weight=10, opposite_weight=0.5)
user2_vector = calculate_weighted_average_vector(user2['general_preference'], selected_weight=10, opposite_weight=0.5)


if user1_vector is not None and user2_vector is not None:
    user1_vector = user1_vector.reshape(1, -1)
    user2_vector = user2_vector.reshape(1, -1)
    similarity = cosine_similarity(user1_vector, user2_vector)[0][0]
    print(f"Similarity between User {user1['user_id']} and User {user2['user_id']}: {similarity}")
