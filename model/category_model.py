from gensim.models import Word2Vec
import json

#------------------------ make general_preference model ---------------------

file_path = '../data/user_category.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Prepare text data for Word2Vec training
room_sentences = []
travel_sentences = []
dining_sentences = []
shopping_sentences = []
for preference in data[0]['category_preference']:
    # print(preference)
    for key, value in preference.items():
        if "room" in key:
            room_sentences.append(value)
        elif "travel" in key:
            travel_sentences.append(value)
        elif "dining" in key:
            dining_sentences.append(value)
        elif "shopping" in key:
            shopping_sentences.append(value)

# print(room_sentences, travel_sentences, dining_sentences, shopping_sentences)
        
# Train Word2Vec model
# Save the trained model
room_model = Word2Vec(room_sentences, vector_size=100, window=5, min_count=1, sg=0)
room_model.save("category_room_model.bin")

travel_model = Word2Vec(travel_sentences, vector_size=100, window=5, min_count=1, sg=0)
travel_model.save("category_travel_model.bin")

dining_model = Word2Vec(dining_sentences, vector_size=100, window=5, min_count=1, sg=0)
dining_model.save("category_dining_model.bin")

shopping_model = Word2Vec(shopping_sentences, vector_size=100, window=5, min_count=1, sg=0)
shopping_model.save("category_shopping_model.bin")
