import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
import json
import numpy as np

file_path = './data/user_data_modify_before.json'
output_file_path = './data/similarity_w2v.json'

with open(file_path, 'r') as file:
    user_data = json.load(file)

# Load the trained Word2Vec model
model = Word2Vec.load("word2vec_model.bin")

# Prepare text data for Word2Vec training
sentences = []
for user in user_data:
    for preference in user['general_preference']:
        for key, value in preference.items():
            sentences.append([key, value['selected'], value['opposite']])
    sentences.extend(user['category_preference'])

# # Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)


# 비교할 단어 리스트
words_to_compare = ["Extrovert", "Introvert", "Organized", "Spontaneous", "Budget-conscious", "Generous"]

# 단어 벡터 추출
word_vectors = np.array([model.wv[word] for word in words_to_compare])

# t-SNE를 사용하여 2차원으로 축소
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
reduced_vectors = tsne.fit_transform(word_vectors)

# 시각화
plt.figure(figsize=(10, 6))
for i, (x, y) in enumerate(reduced_vectors):
    plt.scatter(x, y, marker='o', color='b')
    plt.text(x, y, words_to_compare[i], fontsize=9)

plt.title('Word2Vec Vector Comparison and Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()