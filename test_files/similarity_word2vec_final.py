from gensim.models import Word2Vec
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


file_path = './data/user_data_modify.json'
output_file_path = './data/similarity_w2v.json'

with open(file_path, 'r') as file:
    user_data = json.load(file)


# Prepare text data for Word2Vec training
# 전체 general_preference + selected category_preference 데이터로 학습
sentences = []
for user in user_data:
    # for preference in user['general_preference']:
        # for key, value in preference.items():
            # sentences.append([value['selected'], value['opposite']])
    sentences.append(user['category_preference'])
print(sentences)

# # # Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# Save the trained model
model.save("word2vec_model.bin")

# Load the trained model
model = Word2Vec.load("word2vec_model.bin")

# Calculate average vector for user preferences with weighted selected and opposite preferences
def calculate_weighted_average_vector(preferences, selected_weight, opposite_weight):
    total_vector = np.zeros(model.vector_size)
    count = 0
    for preference in preferences:
        # print(preference)
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
user1 = user_data[0] # me
user2 = user_data[1]

user1_vector = calculate_weighted_average_vector(user1['general_preference'], selected_weight=10, opposite_weight=0.5)
user2_vector = calculate_weighted_average_vector(user2['general_preference'], selected_weight=10, opposite_weight=0.5)


# 벡터 간 유사성 계산 함수
def calculate_vector_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

user1_category_pref = user1["category_preference"]
user2_category_pref = user2["category_preference"]
print(user1_category_pref, user2_category_pref)
print(model.wv.index_to_key)
user1_category_vector = np.mean([model.wv[pref] for pref in user1_category_pref], axis=0)
user2_category_vector = np.mean([model.wv[pref] for pref in user2_category_pref], axis=0)
category_similarity = calculate_vector_similarity(user1_category_vector, user2_category_vector)



if user1_vector is not None and user2_vector is not None:
    user1_vector = user1_vector.reshape(1, -1)
    user2_vector = user2_vector.reshape(1, -1)
    similarity = cosine_similarity(user1_vector, user2_vector)[0][0]
    print(f"Similarity between User {user1['user_id']} and User {user2['user_id']}: {similarity}")
    print(f"Category Preference Similarity: {category_similarity:.4f}")
