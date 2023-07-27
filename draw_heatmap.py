import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

file_path = './user_data_similarity_1.json'
# file_path = './user_data_similarity_2.json'

with open(file_path, 'r') as file:
    data = json.load(file)
# 사용자 수
num_users = len(data)

# 유사도 행렬 초기화
similarity_matrix = np.zeros((num_users, num_users))

# 유사도 행렬 채우기
for i, user_data in enumerate(data):
    user_id_i = user_data["user_id"]
    similarity_i = user_data["similarity"]
    for j, similarity_value in similarity_i.items():
        user_id_j = int(j)
        similarity_matrix[user_id_i - 1, user_id_j - 1] = similarity_value

# 히트맵 그리기
plt.figure(figsize=(8, 6))
sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm', xticklabels=range(1, num_users + 1), yticklabels=range(1, num_users + 1))
plt.title('User Similarity Heatmap')
plt.xlabel('Users')
plt.ylabel('Users')
plt.show()
