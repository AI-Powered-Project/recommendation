import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import Word2Vec
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer


# 데이터 준비
data = [
    {
        "user_id": 3,
        "general_preference": [
            "Introvert",
            "Spontaneous",
            "Budget-conscious",
            "Outdoorsy",
            "Early Bird",
            "Traveler",
            "Intellectual"
        ],
        "category_preference": [
            "Compatibility",
            "Friendly",
            "Communication"
        ]
    },
    {
        "user_id": 4,
        "general_preference": [
            "Introvert",
            "Spontaneous",
            "Budget-conscious",
            "Indoorsy",
            "Night Owl",
            "Traveler",
            "Intellectual"
        ],
        "category_preference": [
            "Friendly",
            "Communication",
            "Patient"
        ]
    },
    {
        "user_id": 9,
        "general_preference": [
            "Extrovert",
            "Organized",
            "Generous",
            "Outdoorsy",
            "Night Owl",
            "Traveler",
            "Fun-loving"
        ],
        "category_preference": [
            "Respectful",
            "Compatibility",
            "Trustworthy"
        ]
    }
]

# 벡터화
general_preference_texts = [' '.join(pref) for user in data for pref in user["general_preference"]]
category_preference_texts = [' '.join(pref) for user in data for pref in user["category_preference"]]

tfidf_vectorizer = TfidfVectorizer()
general_tfidf = tfidf_vectorizer.fit_transform(general_preference_texts)
category_tfidf = tfidf_vectorizer.fit_transform(category_preference_texts)

# 모든 선호도 텍스트를 하나의 리스트로 합침
all_preferences = general_preference_texts + category_preference_texts

# Word2Vec 모델 학습
model = Word2Vec([pref.split() for pref in all_preferences], vector_size=2, window=3, min_count=1, sg=1)

# 벡터 추출
preference_vectors = np.array([model.wv[pref.split()].mean(axis=0) for pref in all_preferences])

# PCA를 사용하여 차원 축소
scaler = StandardScaler()
preference_vectors_scaled = scaler.fit_transform(preference_vectors)
pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(preference_vectors_scaled)

# 시각화
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(reduced_vectors[:len(general_preference_texts), 0], reduced_vectors[:len(general_preference_texts), 1], c='blue', marker='o')
for i, user_id in enumerate([user["user_id"] for user in data]):
    plt.annotate(user_id, (reduced_vectors[i, 0], reduced_vectors[i, 1]), textcoords="offset points", xytext=(-10,5), ha='center')

plt.title('General Preferences (Word2Vec)')
plt.xlabel('PCA Dimension 1')
plt.ylabel('PCA Dimension 2')

plt.subplot(1, 2, 2)
plt.scatter(reduced_vectors[len(general_preference_texts):, 0], reduced_vectors[len(general_preference_texts):, 1], c='green', marker='s')
for i, user_id in enumerate([user["user_id"] for user in data]):
    plt.annotate(user_id, (reduced_vectors[i+len(general_preference_texts), 0], reduced_vectors[i+len(general_preference_texts), 1]), textcoords="offset points", xytext=(-10,5), ha='center')

plt.title('Category Preferences (Word2Vec)')
plt.xlabel('PCA Dimension 1')
plt.ylabel('PCA Dimension 2')

plt.tight_layout()
plt.show()