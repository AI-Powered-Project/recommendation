from gensim.models import Word2Vec
from gensim.models import KeyedVectors
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


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

# # Save the trained model
# # model.save("word2vec_model.bin")

# # Load the trained model
# model = Word2Vec.load("word2vec_model.bin")

# Calculate average vector for user preferences with weighted selected and opposite preferences
def calculate_weighted_average_vector(preferences, selected_weight, opposite_weight):
    total_vector = np.zeros(model.vector_size)
    count = 0
    for preference in preferences:
        print(preference)
        for key, value in preference.items():
            try:
                total_vector += selected_weight * model.wv[value['selected']]
                total_vector += opposite_weight * model.wv[value['opposite']]
                count += 2
            except KeyError:
                pass
    if count == 0:
        return None
    return total_vector / count

# Calculate and print similarity between users
# for i, user1 in enumerate(user_data):
    # for j, user2 in enumerate(user_data[i+1:], i+1):
user1 = user_data[0]
user2 = user_data[1]

user1_vector = calculate_weighted_average_vector(user1['general_preference'], selected_weight=2, opposite_weight=0.5)
user2_vector = calculate_weighted_average_vector(user2['general_preference'], selected_weight=2, opposite_weight=0.5)


user1_category_pref = user1["category_preference"]
user2_category_pref = user2["category_preference"]


if user1_vector is not None and user2_vector is not None:
    user1_vector = user1_vector.reshape(1, -1)
    user2_vector = user2_vector.reshape(1, -1)
    similarity = cosine_similarity(user1_vector, user2_vector)[0][0]
    print(f"Similarity between User {user1['user_id']} and User {user2['user_id']}: {similarity}")