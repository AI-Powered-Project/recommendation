import random
import json

# General preferences options
general_preference_options = [
    "Personality : Extrovert vs. Introvert",
    "Style : Organized vs. Spontaneous",
    "Financial : Budget-conscious vs. Generous",
    "Behavior : Outdoorsy vs. Indoorsy",
    "Chronotype : Early-Bird vs. Night-Owl",
    "Adventurousness : Traveler vs. Homebody",
    "Disposition : Intellectual vs. Fun-loving",
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

def generate_user_json(user_id, gender, birth, location):
    general_preferences = []

    for preference_option in general_preference_options:
        category, data = preference_option.split(" : ")
        left, right = data.split(" vs. ")
        selected = random.choice([left, right])
        opposite = right if selected == left else left
        category = {
           category: {
                "selected": selected,
                "opposite": opposite
            }
        }
        general_preferences.append(category)

    category_preferences = random.sample(room_category_preference_options, 3)
    
    user_data = {
        "user_id": user_id,
        "gender": gender,
        "birth": birth,
        "location": location,
        "general_preference": general_preferences,
        "category_preference": category_preferences
    }

    return user_data

# Generate multiple user JSONs
num_users = 10  # Specify the number of users you want to generate

user_jsons = []
for i in range(num_users):
    user_json = generate_user_json(i + 1, random.choice(["Male", "Female", "Others"]), random.randint(1970, 2005), "City" + str(i))
    user_jsons.append(user_json)

# 데이터를 JSON 형식으로 변환하여 저장
with open('data/user_data_modify_before.json', 'w') as json_file:
    json.dump(user_jsons, json_file, indent=2)

print("JSON 파일이 생성되었습니다.")
