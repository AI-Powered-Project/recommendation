import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

file_path = '.data/user_data.json'
output_file_path = '.data/user_data_similarity_2.json'

with open(file_path, 'r') as file:
    users = json.load(file)

# 벡터화를 위한 전처리 함수
def preprocess_preferences(preferences):
    return ' '.join(preferences)

# 벡터화를 위한 전처리된 데이터 생성
preferences_list = [preprocess_preferences(user['general_preference']) + ' ' +
                    preprocess_preferences(user['category_preference'])
                    for user in users]

# 벡터화 수행
vectorizer = CountVectorizer()
preferences_matrix = vectorizer.fit_transform(preferences_list)

# 코사인 유사도 계산
# cosine_similarities = cosine_similarity(preferences_matrix)

# t-SNE를 사용하여 2D로 차원 축소
tsne = TSNE(n_components=2, perplexity=9, random_state=0)  # perplexity 값을 조정해보세요
preferences_tsne = tsne.fit_transform(preferences_matrix.toarray())

# 시각화
plt.figure(figsize=(10, 8))
plt.scatter(preferences_tsne[:, 0], preferences_tsne[:, 1], c='blue', marker='o')
for i, user in enumerate(users):
    plt.annotate(user['user_id'], (preferences_tsne[i, 0], preferences_tsne[i, 1]), fontsize=10, alpha=0.75)
plt.title('t-SNE Visualization of User Preferences')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
