from gensim.models import Word2Vec
import json

#------------------------ make general_preference model ---------------------

file_path = '../data/user_general.json'
with open(file_path, 'r') as file:
    user_data = json.load(file)


# Prepare text data for Word2Vec training
sentences = []
for user in user_data:
    for preference in user['general_preference']:
        for key, value in preference.items():
            sentences.append([value['selected'], value['opposite']])
# print(sentences)

# # # Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# Save the trained model
model.save("general_model.bin")


#------------------------ visualization ---------------------

import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Word2Vec model load
model = Word2Vec.load("general_model.bin")  # Model path.

# Extracting words and vectors from the model
words = list(model.wv.index_to_key)
vectors = np.array([model.wv[word] for word in words])  # Convert to 2D array

# Use t-SNE to reduce vectors in two dimensions
perplexity_value = min(30, len(words) - 1)
tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity_value)
reduced_vectors = tsne.fit_transform(vectors)

# visualization
plt.figure(figsize=(12, 8))
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], marker='o', color='b', alpha=0.7)
for i, word in enumerate(words):
    plt.annotate(word, (reduced_vectors[i, 0], reduced_vectors[i, 1]), fontsize=9)

plt.title('Word2Vec Word Embedding Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()