import json
from user_category_calculator import UserSimilarityCalculator

# JSON input for multiple users
users_data = [
        {
            "user_id": 1,
            "category_preference": [
                "Respectful",
                "Cooperative"
            ]
        },
        {
            "user_id": 2,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Responsible"
            ]
        },
        {
            "user_id": 3,
            "category_preference": [
                "Friendly",
                "Cooperative",
                "Patient"
            ]
        },
        {
            "user_id": 4,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Friendly"
            ]
        },
        {
            "user_id": 5,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Respectful"
            ]
        },
        {
            "user_id": 6,
            "category_preference": [
                "Respectful",
                "Cooperative",
                "Responsible"
            ]
        },
    # ... other users
]
    

model_path = "category_room_model.bin"
calculator = UserSimilarityCalculator(model_path)

num_users = len(users_data)
for i in range(1, num_users):
    user1 = users_data[0]  # me
    user2 = users_data[i]

    user1_category_pref = user1["category_preference"]
    user2_category_pref = user2["category_preference"]

    category_similarity = calculator.calculate_category_similarity(user1_category_pref, user2_category_pref)
    print(f"Similarity between User Me and User {i+1}: {round(category_similarity, 4)}")