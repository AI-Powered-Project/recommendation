from user_calculator import UserSimilarityCalculator

# JSON input for multiple users
users_general_data = [
    [
        {
        "Personality": {
          "selected": "Introvert",
          "opposite": "Extrovert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Spontaneous",
          "opposite": "Organized"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Generous",
          "opposite": "Budget-conscious"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Indoorsy",
          "opposite": "Outdoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Spontaneous",
          "opposite": "Organized"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Homebody",
          "opposite": "Traveler"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
       {
        "Personality": {
          "selected": "Introvert",
          "opposite": "Extrovert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Outdoorsy",
          "opposite": "Indoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Early-Bird",
          "opposite": "Night-Owl"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Intellectual",
          "opposite": "Fun-loving"
        }
      },
    ],
    [
        {
        "Personality": {
          "selected": "Extrovert",
          "opposite": "Introvert"
        }
      },
      {
        "Style": {
          "selected": "Organized",
          "opposite": "Spontaneous"
        }
      },
      {
        "Financial": {
          "selected": "Budget-conscious",
          "opposite": "Generous"
        }
      },
      {
        "Behavior": {
          "selected": "Indoorsy",
          "opposite": "Outdoorsy"
        }
      },
      {
        "Chronotype": {
          "selected": "Night-Owl",
          "opposite": "Early-Bird"
        }
      },
      {
        "Adventurousness": {
          "selected": "Traveler",
          "opposite": "Homebody"
        }
      },
      {
        "Disposition": {
          "selected": "Fun-loving",
          "opposite": "Intellectual"
        }
      },
    ],
    # ... other users
]

users_data_category = [
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

# General Preference Process
general_calculator = UserSimilarityCalculator("./models/general_model.bin")
# Call general preference calculation function
general_similarity = general_calculator.general_result(users_general_data)
# print(general_similarity)


# Category Preference Process
party_type = "room" # "travel", "dining", "shopping"

if party_type == "room" : # if user select find roommate
    category_calculator = UserSimilarityCalculator("./models/category_room_model.bin")
elif party_type == "travel": # if user select find travelmate
    category_calculator = UserSimilarityCalculator("./models/category_travel_model.bin")
elif party_type == "dining": # if user select find diningmate
    category_calculator = UserSimilarityCalculator("./models/category_dining_model.bin")
elif party_type == "shopping": # if user select find shoppingmate
    category_calculator = UserSimilarityCalculator("./models/category_shopping_model.bin")

# Call category preference calculation function
category_similarity = category_calculator.get_result(users_data_category)
# print(category_similarity)

final_similarity = general_similarity + category_similarity
print(final_similarity)