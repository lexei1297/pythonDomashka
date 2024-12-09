import string
from pymorphy2 import MorphAnalyzer
import matplotlib.pyplot as plt
from collections import Counter
import re


# 1. Функция чтения отзывов из файлов
def load_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Разделение отзывов по пустой строке
    reviews = [review.strip() for review in content.split('\n\n') if review.strip()]
    return reviews


# 2. Функции предобработки текста
def preprocess_text(text):
    # Преобразование в нижний регистр
    text = text.lower()
    # Удаление пунктуации
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Удаление лишних пробелов
    text = ' '.join(text.split())
    return text


def lemmatize_and_filter(text, morph):
    # Удаление предлогов и приведение к нормальной форме
    words = text.split()
    lemmatized_words = [morph.parse(word)[0].normal_form for word in words if morph.parse(word)[0].tag.POS != 'PREP']
    return lemmatized_words


# 3. Подготовка данных
def prepare_reviews(reviews, morph):
    processed_reviews = []
    for review in reviews:
        preprocessed = preprocess_text(review)
        lemmatized = lemmatize_and_filter(preprocessed, morph)
        word_freq = Counter(lemmatized)
        processed_reviews.append(word_freq)
    return processed_reviews


# 4. Гистограмма частот
def plot_histogram(word_freq, title):
    plt.figure(figsize=(10, 6))
    words, counts = zip(*word_freq.items())
    plt.bar(words, counts, color='skyblue')
    plt.title(title)
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# 5. Пересечения и уникальные слова
def find_unique_words(pos_dicts, neg_dicts):
    pos_words = set(word for d in pos_dicts for word in d.keys())
    neg_words = set(word for d in neg_dicts for word in d.keys())
    unique_positive = pos_words - neg_words
    unique_negative = neg_words - pos_words
    return unique_positive, unique_negative


# Основной блок
if name == "main":
    morph = MorphAnalyzer()

    # Загрузка данных из файлов
    positive_reviews = load_reviews('positive.txt')
    negative_reviews = load_reviews('negative.txt')

    # Обработка отзывов
    processed_negative = prepare_reviews(negative_reviews, morph)
    processed_positive = prepare_reviews(positive_reviews, morph)

    # Визуализация
    for i, freq_dict in enumerate(processed_negative, 1):
        plot_histogram(freq_dict, f"Гистограмма частот слов - Отрицательный отзыв {i}")
    for i, freq_dict in enumerate(processed_positive, 1):
        plot_histogram(freq_dict, f"Гистограмма частот слов - Положительный отзыв {i}")

    # Поиск уникальных слов
    unique_positive, unique_negative = find_unique_words(processed_positive, processed_negative)

    print("Уникальные слова в положительных отзывах:", unique_positive)
    print("Уникальные слова в отрицательных отзывах:", unique_negative)