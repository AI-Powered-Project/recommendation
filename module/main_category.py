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
    
party_type = "room" # "travel", "dining", "shopping"

if party_type == "room" : # if user select find roommate
    calculator = UserSimilarityCalculator("./models/category_room_model.bin")
elif party_type == "travel": # if user select find travelmate
    calculator = UserSimilarityCalculator("./models/category_travel_model.bin")
elif party_type == "dining": # if user select find diningmate
    calculator = UserSimilarityCalculator("./models/category_dining_model.bin")
elif party_type == "shopping": # if user select find shoppingmate
    calculator = UserSimilarityCalculator("./models/category_shopping_model.bin")

# Call category calculation function
category_similarity = calculator.get_result(users_data)
# print(category_similarity)
