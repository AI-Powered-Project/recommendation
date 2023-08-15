import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

users_data = [
        {
            "user_id": 1,
            "category_preference": [
                "Respectful",
                "Cooperative"
            ]
        },
        {
            "user_id": 2,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Responsible"
            ]
        },
        {
            "user_id": 3,
            "category_preference": [
                "Friendly",
                "Cooperative",
                "Patient"
            ]
        },
        {
            "user_id": 4,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Friendly"
            ]
        },
        {
            "user_id": 5,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Respectful"
            ]
        },
        {
            "user_id": 6,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Responsible"
            ]
        },
    # ... other users
]
    

# Load the trained model
model = Word2Vec.load("category_room_model.bin")

# 벡터 간 유사성 계산 함수
def calculate_vector_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

num_users = len(users_data)
for i in range(1, num_users):

        user1 = users_data[0] # me
        user2 = users_data[i]

        user1_category_pref = user1["category_preference"]
        user2_category_pref = user2["category_preference"]

        user1_category_vector = np.mean([model.wv[pref] for pref in user1_category_pref], axis=0)
        user2_category_vector = np.mean([model.wv[pref] for pref in user2_category_pref], axis=0)
        category_similarity = calculate_vector_similarity(user1_category_vector, user2_category_vector)
        print(f"Similarity between User Me and User {i+1}: {round(category_similarity,4)}")





