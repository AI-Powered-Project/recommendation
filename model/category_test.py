import json
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

#----------------------- dummy data loading ----------------------------

file_path = '../data/user_category_input.json'
with open(file_path, 'r') as file:
    user_data = json.load(file)

#-----------------------------------------------------------------------
    

# Load the trained model
model = Word2Vec.load("category_room_model.bin")

# 벡터 간 유사성 계산 함수
def calculate_vector_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]


user1 = user_data[0] # me
user1_category_pref = user1["category_preference"]
# 여기서 유저 리스트를 불러와서 user1 <-> users 비교한 후 DB에 general preference n개 저장
user2 = user_data[1]
user2_category_pref = user2["category_preference"]

user1_category_vector = np.mean([model.wv[pref] for pref in user1_category_pref], axis=0)
user2_category_vector = np.mean([model.wv[pref] for pref in user2_category_pref], axis=0)
category_similarity = calculate_vector_similarity(user1_category_vector, user2_category_vector)
print(f"Category Preference Similarity: {category_similarity:.4f}")
