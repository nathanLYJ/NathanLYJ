import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# NLTK 데이터 다운로드
nltk.download('movie_reviews')

# 특성 추출 함수
def extract_features(words):
    return dict([(word, True) for word in words])

# 데이터 준비
positive_fileids = movie_reviews.fileids('pos')
negative_fileids = movie_reviews.fileids('neg')

positive_features = [(extract_features(movie_reviews.words(fileids=[f])), 'pos') for f in positive_fileids]
negative_features = [(extract_features(movie_reviews.words(fileids=[f])), 'neg') for f in negative_fileids]

# 훈련 세트와 테스트 세트 분리
train_features = positive_features[:800] + negative_features[:800]
test_features = positive_features[800:] + negative_features[800:]

# 분류기 훈련
classifier = NaiveBayesClassifier.train(train_features)

# 정확도 평가
print("Accuracy:", accuracy(classifier, test_features))

# 새로운 텍스트 분류

def classify_text(text):
    features = extract_features(text.split())
    return classifier.classify(features)
    
# 예제 리뷰 분류
example_reviews = [
    "This movie was fantastic! I really enjoyed every moment.",
    "I've never been so bored in my life. Terrible acting and plot.",
    "It was okay, not great but not terrible either.",
    "A masterpiece of cinema! This film will be remembered for generations.",
    "I wish I could get my money back. What a waste of time."
]

print("\nExample Reviews Classification:")
for review in example_reviews:
    print(f"Review: {review}")
    print(f"Sentiment: {classify_text(review)}\n")

# 사용자 입력 받기
while True:
    user_review = input("Enter a movie review (or 'quit' to exit): ")
    if user_review.lower() == 'quit':
        break
    print(f"Sentiment: {classify_text(user_review)}\n")

print("Thank you for using the sentiment analyzer!")