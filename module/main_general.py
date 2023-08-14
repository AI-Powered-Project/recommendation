import json
from user_similarity_calculator import UserSimilarityCalculator

# JSON input for multiple users
users_data = [
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

# Initialize the UserSimilarityCalculator with the Word2Vec model
calculator = UserSimilarityCalculator("general_model.bin")

# Calculate and print similarities between users
# num_users = len(users_data)
# for i in range(num_users):
#     for j in range(i + 1, num_users):  # Compare only distinct pairs
#         user1_data = users_data[i]
#         user2_data = users_data[j]
        
#         similarity = calculator.calculate_similarity(user1_data, user2_data)
#         if similarity is not None:
#             print(f"Similarity between User {i + 1} and User {j + 1}: {round(similarity,4)}")


# Calculate and print similarities between me and users
num_users = len(users_data)
for i in range(1, num_users):
        user1_data = users_data[0] # Me
        user2_data = users_data[i]
        
        similarity = calculator.calculate_similarity(user1_data, user2_data)
        if similarity is not None:
            print(f"Similarity between User Me and User {i+1}: {round(similarity,4)}")