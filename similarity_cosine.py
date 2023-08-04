import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


file_path = './user_data.json'
output_file_path = './user_data_similarity_2.json'

with open(file_path, 'r') as file:
    users = json.load(file)


# 벡터화를 위한 전처리 함수
def preprocess_preferences(preferences):
    return ' '.join(preferences)

# 벡터화를 위한 전처리된 데이터 생성
preferences_list = [preprocess_preferences(user['general_preference']) + ' ' +
                    preprocess_preferences(user['category_preference'])
                    for user in users]

# print(preferences_list)

# 벡터화 수행
vectorizer = CountVectorizer()
preferences_matrix = vectorizer.fit_transform(preferences_list)

#----------------------------------------------------------------------------------------------------------

# 코사인 유사도 계산
cosine_similarities = cosine_similarity(preferences_matrix)

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
