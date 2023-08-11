from gensim.models import Word2Vec
import itertools
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np

# Prepare text data for Word2Vec training
# Category preferences options


file_path = '../data/user_data_modify.json'
output_file_path = './data/similarity_w2v.json'

with open(file_path, 'r') as file:
    user_data = json.load(file)


room_category_preference_options = [
    "Cleanliness", "Compatibility", "Respectful", "Trustworthy", "Communication", "Responsible",
    "Cooperative", "Friendly", "Safety-conscious", "Patient"
]

# 가능한 모든 경우의 수 생성
all_combinations = []
for r in range(1, len(room_category_preference_options) + 1):
    combinations = list(itertools.combinations(room_category_preference_options, 3))
    all_combinations.extend(combinations)
    # print(all_combinations)

# # 결과 출력
# for combination in all_combinations:
#     print(list(combination))

# travel_category_preference_options = [
#     "Adventurous", "Responsible", "Respectful", "Punctuality", "Compatibility", "Communication", "Open-minded",
#     "Budget-conscious", "Safety-conscious", "Language-skills"
# ]
# dining_category_preference_options = [
#     "Cleanliness", "Food preferences", "Compatibility", "Punctuality", "Flexibility", "Communication", "Allergies",
#     "Open-minded", "Table-manner", "Meal-sharing",
# ]
# shopping_category_preference_options = [
#     "Budget-conscious", "Savings", "Splitting", "Sharing", "Convenience", "Quality",
#     "Variety", "Coupons", "Deals", "Communication"
# ]

# # # Train Word2Vec model
room_model = Word2Vec(all_combinations, vector_size=100, window=5, min_count=1, sg=0)

# Save the trained model
room_model.save("category_roommate.bin")

# Load the trained model
room_model = Word2Vec.load("category_roommate.bin")

print(room_model.wv.index_to_key)

# 벡터 간 유사성 계산 함수
def calculate_vector_similarity(vec1, vec2):
    return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]


# Calculate and print similarity between users
user1 = user_data[0] # me
user2 = user_data[1]

user1_category_pref = user1["category_preference"]
user2_category_pref = user2["category_preference"]
print(user1_category_pref, user2_category_pref)
user1_category_vector = np.mean([room_model.wv[pref] for pref in user1_category_pref], axis=0)
user2_category_vector = np.mean([room_model.wv[pref] for pref in user2_category_pref], axis=0)
category_similarity = calculate_vector_similarity(user1_category_vector, user2_category_vector)


print(f"Category Preference Similarity: {category_similarity:.4f}")
