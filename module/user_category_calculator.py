import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

class UserSimilarityCalculator:
    def __init__(self, model_path):
        self.model = Word2Vec.load(model_path)

    def calculate_vector_similarity(self, vec1, vec2):
        return cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]

    def calculate_category_similarity(self, user1_category_pref, user2_category_pref):
        user1_category_vector = np.mean([self.model.wv[pref] for pref in user1_category_pref], axis=0)
        user2_category_vector = np.mean([self.model.wv[pref] for pref in user2_category_pref], axis=0)
        return self.calculate_vector_similarity(user1_category_vector, user2_category_vector)
