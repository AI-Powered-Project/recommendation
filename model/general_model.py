from gensim.models import Word2Vec
import json


file_path = '../data/user_general.json'
with open(file_path, 'r') as file:
    user_data = json.load(file)


# Prepare text data for Word2Vec training
sentences = []
for user in user_data:
    for preference in user['general_preference']:
        for key, value in preference.items():
            sentences.append([value['selected'], value['opposite']])
# print(sentences)

# # # Train Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)

# Save the trained model
model.save("general_model.bin")


