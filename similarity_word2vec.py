from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

file_path = './data/user_data.json'
output_file_path = './data/user_data_similarity_3.json'

with open(file_path, 'r') as file:
    users = json.load(file)

# 사용자의 preference를 추출하여 리스트로 저장
all_preferences = []
for user in users:
    preferences = user["general_preference"] + user["category_preference"]
    all_preferences.append(preferences)

# print(all_preferences)

# Word2Vec 모델 학습
model = Word2Vec(sentences=all_preferences, vector_size=100, window=5, min_count=1, sg=1)

# 각 사용자의 preference를 단어 벡터로 변환하여 유사도 계산
user_vectors = []
for preferences in all_preferences:
    vectors = [model.wv[preference] for preference in preferences if preference in model.wv]
    if vectors:
        user_vector = np.mean(vectors, axis=0)
        user_vectors.append(user_vector)

#----------------------------------------------------------------------------------------------------------

# 사용자 간 유사도 계산
cosine_similarities = cosine_similarity(user_vectors)

# 유사도 결과 출력
user_similarities = {user['user_id']: {} for user in users}  # Initialize user_similarities for all user IDs
for i, user1 in enumerate(users):
    for j, user2 in enumerate(users):
        similarity_score = cosine_similarities[i, j]
        user_similarities[user1['user_id']][user2['user_id']] = round(similarity_score *10, 3)
        user_similarities[user2['user_id']][user1['user_id']] = round(similarity_score *10, 3)
        # print(f"Cosine Similarity : {user1['user_id']} and {user2['user_id']}: {similarity_score:.3f}")
        # print(similarity_score)
    # print()


# Update the existing JSON data with similarity information
for user in users:
    user_id = user['user_id']
    user['similarity'] = user_similarities[user_id]

# Save the updated JSON data back to the file
with open(output_file_path, 'w') as file:
    json.dump(users, file, indent=2)
