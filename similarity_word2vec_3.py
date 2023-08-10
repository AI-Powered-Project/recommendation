import json
from gensim.models import Word2Vec
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

file_path = './data/user_data.json'
output_file_path = './data/user_data_w2v_result.json'

with open(file_path, 'r') as file:
    users = json.load(file)

# JSON 데이터

# JSON 데이터에서 값을 추출하여 유사성 계산
user1 = users[0]
user2 = users[1]

# user1_general_pref = [list(item.values())[0] for item in user1["general_preference"]]
# user2_general_pref = [list(item.values())[0] for item in user2["general_preference"]]

user1_general_pref = user1["general_preference"]
user2_general_pref = user2["general_preference"]

user1_category_pref = user1["category_preference"]
user2_category_pref = user2["category_preference"]

# Word2Vec 모델 구축
sentences = [user1_general_pref, user2_general_pref] + [user1_category_pref, user2_category_pref]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)
print(sentences)

# 벡터 간 유사성 계산 함수
def calculate_vector_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

user1_general_vectors = np.mean([model.wv[pref] for pref in user1_general_pref], axis=0)
user2_general_vectors = np.mean([model.wv[pref] for pref in user2_general_pref], axis=0)

user1_category_vector = np.mean([model.wv[pref] for pref in user1_category_pref], axis=0)
user2_category_vector = np.mean([model.wv[pref] for pref in user2_category_pref], axis=0)

# 벡터 간 유사성 계산
general_similarity = calculate_vector_similarity(user1_general_vectors, user2_general_vectors)
category_similarity = calculate_vector_similarity(user1_category_vector, user2_category_vector)

print(f"General Preference Similarity: {general_similarity:.4f}")
print(f"Category Preference Similarity: {category_similarity:.4f}")
