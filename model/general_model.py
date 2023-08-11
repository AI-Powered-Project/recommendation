from gensim.models import Word2Vec
import json

#------------------------ make general_preference model ---------------------

file_path = '../data/user_general.json'
with open(file_path, 'r') as file:
    user_data = json.load(file)


# Prepare text data for Word2Vec training
sentences = []
for preference in user_data[0]['general_preference']:
    for key, value in preference.items():
        sentences.append([value['selected'], value['opposite']])
# print(sentences)

# # # Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# Save the trained model
model.save("general_model.bin")
# print(model.wv.key_to_index) # -> key값 + idx



#------------------------ visualization ---------------------

import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from sklearn.metrics.pairwise import cosine_similarity

# # Word2Vec model load
model = Word2Vec.load("general_model.bin")  # Model path.

# Extracting words and vectors from the model
words = list(model.wv.index_to_key)
vectors = np.array([model.wv[word] for word in words])  # Convert to 2D array

# Use t-SNE to reduce vectors in two dimensions
perplexity_value = min(30, len(words) - 1)
tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity_value)
reduced_vectors = tsne.fit_transform(vectors)

# 단어 간 의미적 유사도 계산
similarities = cosine_similarity(vectors)

# 군집 형성
threshold = 0.8  # 유사도 임계값
clusters = {word: [i] for i, word in enumerate(words)}
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if similarities[i, j] > threshold:
            clusters[words[i]].append(j)
            clusters[words[j]].append(i)

# # visualization
plt.figure(figsize=(12, 8))
for cluster_indices in clusters.values():
    plt.scatter(reduced_vectors[cluster_indices, 0], reduced_vectors[cluster_indices, 1], marker='o', alpha=0.7)

for i, word in enumerate(words):
    plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]), fontsize=9)

plt.title('Word2Vec Word Embedding Clustering Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()
