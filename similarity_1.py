import random
import json

file_path = './user.json'

with open(file_path, 'r') as file:
    users = json.load(file)
    #print(type(data))
    #print(data)


def calculate_similarity(user1, user2):
    general_similarity = len(set(user1['general_preference']) & set(user2['general_preference']))
    category_similarity = len(set(user1['category_preference']) & set(user2['category_preference']))

    total_similarity = general_similarity + category_similarity
    return total_similarity


# 모든 사용자들 간의 유사도 계산
user_similarities = {user['user_id']: {} for user in users}  # Initialize user_similarities for all user IDs
for i, user1 in enumerate(users):
    for j in range(i + 1, len(users)):
        user2 = users[j]
        similarity = calculate_similarity(user1, user2)
        user_similarities[user1['user_id']][user2['user_id']] = similarity
        user_similarities[user2['user_id']][user1['user_id']] = similarity

# 결과 출력
for user_id, similarities in user_similarities.items():
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    print(f"User {user_id}:")
    for other_user_id, similarity in sorted_similarities:
        if other_user_id != user_id:
            print(f" - User {other_user_id}, 유사도: {similarity}")
    print()
