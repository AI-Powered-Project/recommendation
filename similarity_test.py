####### 텍스트 유사도 측정 ######
from sklearn.feature_extraction.text import TfidfVectorizer
sentences = ("이 요리 의 레시피 를 알려줘.",
        "이 요리 어떻게 만드는 지 알려줘.")
tfidf_vectorizer = TfidfVectorizer()

# 문장 벡터화 하기(사전 만들기)
tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)

### 코사인 유사도 ###
from sklearn.metrics.pairwise import cosine_similarity
# 첫 번째와 두 번째 문장 비교
cos_similar = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
print("코사인 유사도 측정")
print(cos_similar)
