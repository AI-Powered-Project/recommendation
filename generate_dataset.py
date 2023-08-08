import random
import json
import csv

# General preferences options
general_preference_options = [
    "Extrovert vs. Introvert", 
    "Organized vs. Spontaneous",
    "Budget-conscious vs. Generous",
    "Outdoorsy vs. Indoorsy",
    "Early Bird vs. Night Owl",
    "Traveler vs. Homebody",
    "Intellectual vs. Fun-loving",
]

# Category preferences options
room_category_preference_options = [
    "Cleanliness", "Compatibility", "Respectful", "Trustworthy", "Communication", "Responsible",
    "Cooperative", "Friendly", "Safety-conscious", "Patient"
]
travel_category_preference_options = [
    "Adventurous", "Responsible", "Respectful", "Punctuality", "Compatibility", "Communication", "Open-minded",
    "Budget-conscious", "Safety-conscious", "Language-skills"
]
dining_category_preference_options = [
    "Cleanliness", "Food preferences", "Compatibility", "Punctuality", "Flexibility", "Communication", "Allergies",
    "Open-minded", "Table-manner", "Meal-sharing",
]
shopping_category_preference_options = [
    "Budget-conscious", "Savings", "Splitting", "Sharing", "Convenience", "Quality",
    "Variety", "Coupons", "Deals", "Communication"
]

# Generate 10 user sets
users = []
for i in range(1, 11):
    user_set = {
        "user_id": i,
        "gender": random.choice(["Male", "Female","Others"]),
        "birth": random.randint(1980, 2010),
        "location":"SanFrancisco",

    }
    # Select one option for each general_preference item
    user_set["general_preference"] = [
        random.choice(pref.split(" vs. ")) for pref in general_preference_options
    ]

    # Randomly select 5 categories for category_preference
    user_set["category_preference"] = random.sample(room_category_preference_options, 3)
    users.append(user_set)

# Print the user sets
for user in users:
    print(user)



# 데이터를 JSON 형식으로 변환하여 저장
with open('data/user_data.json', 'w') as json_file:
    json.dump(users, json_file, indent=2)

print("JSON 파일이 생성되었습니다.")



# # CSV 파일에 저장할 헤더 정의
# field_names = ["user_id", "gender", "birth", "location", "general_preference", "category_preference"]
#
# # 데이터를 CSV 파일로 저장
# with open('user_data.csv', 'w', newline='') as csv_file:
#     writer = csv.DictWriter(csv_file, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(users)
#
# print("CSV 파일이 생성되었습니다.")
