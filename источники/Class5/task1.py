import os
import string
import re
from pymorphy2 import MorphAnalyzer
import matplotlib.pyplot as plt
from collections import Counter

morph = MorphAnalyzer()

reviews_dir = "reviews"

prepositions = {"то", "в", "за", "как", "на", "к", "от", "с", "до", "из", "перед", "за", "по", "через", "около", "между", "над", "под", "у", "без", "для", "из-за", "вопреки", "помимо", "сквозь", "посредством"}

def preprocess_text(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())
    return text

def lemmatize_and_remove_prepositions(text):

    words = text.split()
    lemmatized_words = []
    for word in words:
        p = morph.parse(word)[0]
        if p.normal_form not in prepositions:
            lemmatized_words.append(p.normal_form)
    return " ".join(lemmatized_words)

def create_word_frequency_dict(text):

    words = text.split()
    return dict(Counter(words))


reviews_data = []
for filename in os.listdir(reviews_dir):
    filepath = os.path.join(reviews_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        sentiment = "positive" if "positive" in filename else "negative"
        for line in f:
            processed_text = preprocess_text(line)
            lemmatized_text = lemmatize_and_remove_prepositions(processed_text)
            word_frequencies = create_word_frequency_dict(lemmatized_text)
            reviews_data.append({"sentiment": sentiment, "text": lemmatized_text, "word_frequencies": word_frequencies})



for review in reviews_data:
    plt.figure(figsize=(10, 6))
    plt.bar(review["word_frequencies"].keys(), review["word_frequencies"].values())
    plt.title(f"Гистограмма частоты слов ({review['sentiment']} отзыв)")
    plt.xlabel("Слова")
    plt.ylabel("Частота")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()



positive_words = set()
negative_words = set()

for review in reviews_data:
    if review["sentiment"] == "positive":
        positive_words.update(review["word_frequencies"].keys())
    else:
        negative_words.update(review["word_frequencies"].keys())

intersection = positive_words.intersection(negative_words)
only_positive = positive_words - intersection
only_negative = negative_words - intersection

print("Слова в обоих типах отзывов:", intersection)
print("Слова в позитивных отзывах:", only_positive)
print("Слова в негативных отзывах:", only_negative)
