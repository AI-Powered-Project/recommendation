import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

class UserCategorySimilarityCalculator:
    def __init__(self, model_path):
        self.model = Word2Vec.load(model_path)

    def calculate_vector_similarity(self, vec1, vec2):
        return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

    def calculate_category_similarity(self, user1_category_pref, user2_category_pref):
        user1_category_vector = np.mean([self.model.wv[pref] for pref in user1_category_pref], axis=0)
        user2_category_vector = np.mean([self.model.wv[pref] for pref in user2_category_pref], axis=0)
        return self.calculate_vector_similarity(user1_category_vector, user2_category_vector)

    def get_result(self, users_data):
        num_users = len(users_data)
        category_sum = 0.0
        for i in range(1, num_users):
            user1 = users_data[0]  # me
            user2 = users_data[i]

            user1_category_pref = user1["category_preference"]
            user2_category_pref = user2["category_preference"]

            category_similarity = self.calculate_category_similarity(user1_category_pref, user2_category_pref)
            category_sum += category_similarity
            # print(f"Similarity between User Me and User {i+1}: {round(category_similarity, 4)}")
        return round(category_sum/num_users,4)