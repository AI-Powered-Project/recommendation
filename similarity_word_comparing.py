import random
import csv
import json

file_path = './user_data.json'
output_file_path = './user_data_similarity_1.json'

with open(file_path, 'r') as file:
    users = json.load(file)

# Check how many words are the same in words
def calculate_similarity(user1, user2):
    general_similarity = len(set(user1['general_preference']) & set(user2['general_preference']))
    category_similarity = len(set(user1['category_preference']) & set(user2['category_preference']))

    total_similarity = general_similarity + category_similarity
    return total_similarity


# Calculation of similarity between all users
user_similarities = {user['user_id']: {} for user in users}  # Initialize user_similarities for all user IDs
for i, user1 in enumerate(users):
    for j in range(i, len(users)):
        user2 = users[j]
        similarity = calculate_similarity(user1, user2)
        user_similarities[user1['user_id']][user2['user_id']] = similarity
        user_similarities[user2['user_id']][user1['user_id']] = similarity

# Store similarity results in a list
similarity_results = []
for user_id, similarities in user_similarities.items():
    user_result = {"similarity": []}
    for other_user_id, similarity in similarities.items():
        # print(user_id, other_user_id)
        if other_user_id != user_id:
            user_result["similarity"].append(similarity)
        else : # user_idx
            user_result["similarity"].append('.')
    similarity_results.append(user_result)
print(similarity_results)


# Calculation of similarity between all users
user_similarities = {user['user_id']: {} for user in users}  # Initialize user_similarities for all user IDs
for i, user1 in enumerate(users):
    for j in range(i, len(users)):
        user2 = users[j]
        similarity = calculate_similarity(user1, user2)
        user_similarities[user1['user_id']][user2['user_id']] = similarity
        user_similarities[user2['user_id']][user1['user_id']] = similarity

# Update the existing JSON data with similarity information
for user in users:
    user_id = user['user_id']
    user['similarity'] = user_similarities[user_id]

# Save the updated JSON data back to the file
with open(output_file_path, 'w') as file:
    json.dump(users, file, indent=2)
