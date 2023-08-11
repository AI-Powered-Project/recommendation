import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

#----------------------- dummy data loading ----------------------------

file_path = '../data/user_general_2.json'
with open(file_path, 'r') as file:
    users = json.load(file)

#-----------------------------------------------------------------------
    

# Load the trained model
model = Word2Vec.load("general_model.bin")

# Calculate average vector for user preferences with weighted selected and opposite preferences
def calculate_weighted_average_vector(preferences, selected_weight, opposite_weight):
    total_vector = np.zeros(model.vector_size)
    count = 0
    for preference in preferences:
        # print(preference)
        for key, value in preference.items():
            # print(key, value)
            try:
                total_vector += selected_weight * model.wv[value['selected']]
                total_vector += opposite_weight * model.wv[value['opposite']]
                count += 2
            except KeyError:
                pass
    if count == 0:
        return None
    return total_vector / count



# 사용자 간 유사도 계산
user_similarities = {user['user_id']: {} for user in users}  # Initialize user_similarities for all user IDs
for i, user1 in enumerate(users):
    for j, user2 in enumerate(users):
        if i< j:
            user1 = users[i]
            user2 = users[j]
            user1_vector = calculate_weighted_average_vector(user1['general_preference'], selected_weight=10, opposite_weight=0.5)
            user2_vector = calculate_weighted_average_vector(user2['general_preference'], selected_weight=10, opposite_weight=0.5)

            # Calculate and print similarity between users
            if user1_vector is not None and user2_vector is not None:
                user1_vector = user1_vector.reshape(1, -1)
                user2_vector = user2_vector.reshape(1, -1)
                similarity = cosine_similarity(user1_vector, user2_vector)[0][0]
                print(f"Similarity between User {user1['user_id']} and User {user2['user_id']}: {similarity}")
