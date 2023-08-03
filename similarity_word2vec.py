from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

file_path = './user_data.json'
output_file_path = './user_data_similarity_3.json'

with open(file_path, 'r') as file:
    users = json.load(file)

# 사용자의 preference를 추출하여 리스트로 저장
all_preferences = []
for user in users:
    preferences = user["general_preference"] + user["category_preference"]
    all_preferences.append(preferences)

# Word2Vec 모델 학습
model = Word2Vec(sentences=all_preferences, vector_size=100, window=5, min_count=1, sg=1)

# 각 사용자의 preference를 단어 벡터로 변환하여 유사도 계산
user_vectors = []
for preferences in all_preferences:
    vectors = [model.wv[preference] for preference in preferences if preference in model.wv]
    if vectors:
        user_vector = np.mean(vectors, axis=0)
        user_vectors.append(user_vector)

# 사용자 간 유사도 계산
similarity_matrix = cosine_similarity(user_vectors)

# 사용자 간 유사도 출력
for i in range(len(users)):
    for j in range(i+1, len(users)):
        similarity = similarity_matrix[i][j]
        print(f"사용자 {users[i]['user_id']}과(와) 사용자 {users[j]['user_id']}의 preference 유사도: {similarity:.4f}")
