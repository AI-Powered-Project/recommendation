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
calculator = UserSimilarityCalculator("./models/general_model.bin")
similarity = calculator.general_result(users_data)
# print(similarity)