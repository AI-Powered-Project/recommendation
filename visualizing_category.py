import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
from gensim.models import Word2Vec
from adjustText import adjust_text

# JSON 데이터에서 "room_category_preference"에 해당하는 단어 추출
data = [
    {
        "category_preference": [
            {
                "room_category_preference": [
                    "Cleanliness", "Compatibility", "Respectful", "Trustworthy", "Communication", "Responsible",
                    "Cooperative", "Friendly", "Safety-conscious", "Patient"
                ]
            },
            {
                "travel_category_preference": [
                    "Adventurous", "Responsible", "Respectful", "Punctuality", "Compatibility", "Communication", "Open-minded",
                "Budget-conscious", "Safety-conscious", "Language-skills"
                ]
            },
            {
                "dining_category_preference": [
                    "Cleanliness", "Food preferences", "Compatibility", "Punctuality", "Flexibility", "Communication", "Allergies",
                    "Open-minded", "Table-manner", "Meal-sharing"
                ]
            },
            {
                "shopping_category_preference": [
                    "Budget-conscious", "Savings", "Splitting", "Sharing", "Convenience", "Quality",
                "Variety", "Coupons", "Deals", "Communication"
                ]
            }
        ]
    }
]

room_category_preference = data[0]["category_preference"][0]["room_category_preference"]
travel_category_preference = data[0]["category_preference"][1]["travel_category_preference"]
dining_category_preference = data[0]["category_preference"][2]["dining_category_preference"]
shopping_category_preference = data[0]["category_preference"][3]["shopping_category_preference"]

# Word2Vec 모델 로드
room_model = Word2Vec.load("./model/category_room_model.bin")  # 모델 경로를 지정하세요.
travel_model = Word2Vec.load("./model/category_travel_model.bin")  # 모델 경로를 지정하세요.
dining_model = Word2Vec.load("./model/category_dining_model.bin")  # 모델 경로를 지정하세요.
shopping_model = Word2Vec.load("./model/category_shopping_model.bin")  # 모델 경로를 지정하세요.

# 각 카테고리에 해당하는 단어들에 대한 벡터 추출
room_word_vectors = [room_model.wv[word] for word in room_category_preference]
travel_word_vectors = [travel_model.wv[word] for word in travel_category_preference]
dining_word_vectors = [dining_model.wv[word] for word in dining_category_preference]
shopping_word_vectors = [shopping_model.wv[word] for word in shopping_category_preference]

# t-SNE를 사용하여 2차원으로 벡터 축소
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
room_word_vectors = np.array(room_word_vectors)
reduced_room_vectors = tsne.fit_transform(room_word_vectors)
# travel_word_vectors = np.array(travel_word_vectors)
# reduced_travel_vectors = tsne.fit_transform(travel_word_vectors)
# dining_word_vectors = np.array(dining_word_vectors)
# reduced_dining_vectors = tsne.fit_transform(dining_word_vectors)
# shopping_word_vectors = np.array(shopping_word_vectors)
# reduced_shopping_vectors = tsne.fit_transform(shopping_word_vectors)

# 각 카테고리별 시각화
plt.figure(figsize=(12, 8))

# 각 카테고리별 점 색상 설정
room_color = 'blue'
travel_color = 'green'
dining_color = 'red'
shopping_color = 'purple'

# 방 카테고리
room_scatter = plt.scatter(reduced_room_vectors[:, 0], reduced_room_vectors[:, 1], marker='o', color=room_color, alpha=0.7)
room_texts = [plt.text(reduced_room_vectors[i, 0], reduced_room_vectors[i, 1], room_category_preference[i], fontsize=9, color=room_color) for i in range(len(room_category_preference))]

# 여행 카테고리
# travel_scatter = plt.scatter(reduced_travel_vectors[:, 0], reduced_travel_vectors[:, 1], marker='o', color=travel_color, alpha=0.7)
# travel_texts = [plt.text(reduced_travel_vectors[i, 0], reduced_travel_vectors[i, 1], travel_category_preference[i], fontsize=9, color=travel_color) for i in range(len(travel_category_preference))]

# # 식사 카테고리
# dining_scatter = plt.scatter(reduced_dining_vectors[:, 0], reduced_dining_vectors[:, 1], marker='o', color=dining_color, alpha=0.7)
# dining_texts = [plt.text(reduced_dining_vectors[i, 0], reduced_dining_vectors[i, 1], dining_category_preference[i], fontsize=9, color=dining_color) for i in range(len(dining_category_preference))]

# # 쇼핑 카테고리
# shopping_scatter = plt.scatter(reduced_shopping_vectors[:, 0], reduced_shopping_vectors[:, 1], marker='o', color=shopping_color, alpha=0.7)
# shopping_texts = [plt.text(reduced_shopping_vectors[i, 0], reduced_shopping_vectors[i, 1], shopping_category_preference[i], fontsize=9, color=shopping_color) for i in range(len(shopping_category_preference))]

# 텍스트 위치 조정
adjust_text(room_texts, arrowprops=dict(arrowstyle='-', color=room_color))
# adjust_text(travel_texts, arrowprops=dict(arrowstyle='-', color=travel_color))
# adjust_text(dining_texts, arrowprops=dict(arrowstyle='-', color=dining_color))
# adjust_text(shopping_texts, arrowprops=dict(arrowstyle='-', color=shopping_color))

plt.title('Word2Vec Word Embedding Visualization')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.legend(["Room", "Travel", "Dining", "Shopping"])
plt.show()