import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

class UserSimilarityCalculator:
    def __init__(self, model_path):
        self.model = Word2Vec.load(model_path)

    def calculate_weighted_average_vector(self, preferences, selected_weight, opposite_weight):
        total_vector = np.zeros(self.model.vector_size)
        count = 0
        for preference in preferences:
            for key, value in preference.items():
                try:
                    total_vector += selected_weight * self.model.wv[value['selected']]
                    total_vector += opposite_weight * self.model.wv[value['opposite']]
                    count += 2
                except KeyError:
                    pass
        if count == 0:
            return None
        return total_vector / count

    def calculate_similarity(self, user1_data, user2_data, selected_weight=10, opposite_weight=0.5):
        user1_vector = self.calculate_weighted_average_vector(user1_data, selected_weight, opposite_weight)
        user2_vector = self.calculate_weighted_average_vector(user2_data, selected_weight, opposite_weight)

        if user1_vector is not None and user2_vector is not None:
            user1_vector = user1_vector.reshape(1, -1)
            user2_vector = user2_vector.reshape(1, -1)
            similarity = cosine_similarity(user1_vector, user2_vector)[0][0]
            return similarity
        return None
