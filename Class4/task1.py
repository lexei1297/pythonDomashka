import json
import os

def read_data(path):
    data = open(path, 'rt', encoding='windows-1251').read()
    return data.split('\n')


def word_dictionary(data) -> dict:
    '''
    Напишите программу, которая переберет все слова и занесет их в словарь (назвать его можете как угодно).
    Увеличивайте счётчик при добавлении каждого нового слова, чтобы посчитать сколько раз это слово встречается в тексте.
    '''
    frequency_dic = {}
    for word in data:
        word = word.strip().lower()
        if not word:
            continue
        frequency_dic[word] = frequency_dic.get(word, 0) + 1
    return frequency_dic


def create_chapters_dicts(data):
    deliminators_indicis = [i for i, e in enumerate(data[1:]) if e == '[new chapter]']
    start = 0
    chapter_frequencies = []
    for index in deliminators_indicis:
        chapter_context = data[start:index]
        chapter_frequency = word_dictionary(chapter_context)
        chapter_frequencies.append(chapter_frequency)
        start = index
    last_chapter = data[start:]
    chapter_frequency = word_dictionary(last_chapter)
    chapter_frequencies.append(chapter_frequency)
    return chapter_frequencies

# Пример использования:
file_path = 'war_peace.txt'
data = read_data(file_path)
chapter_frequencies = create_chapters_dicts(data)

# Вывод результатов:
print(json.dumps(chapter_frequencies[0], indent=4, ensure_ascii=False))


import json
import os

def read_data(path):
    data = open(path, 'rt').read()
    return data.split('\n')

def create_chapters_dicts(data):
    chapters = []
    current_chapter = {}
    for line in data:
        if line == "[new chapter]":
            if current_chapter:
                chapters.append(current_chapter)
            current_chapter = {}
        elif line:
            word = line.lower()
            if word in current_chapter:
                current_chapter[word] += 1
            else:
                current_chapter[word] = 1
    if current_chapter:
        chapters.append(current_chapter)
    return chapters

def chapter_frequency(path: str, target_word: str) -> float:
    '''
    Напишите программу, которая посчитает chapter frequency для заданного слова target_word.
    chapter_freq = number_of_chapters_with_target_word / number_of_chapters
    number_of_chapters_with_target_word - общее количество глав
    number_of_chapters - количество глав, в которых встречается target_word
    '''
    data = read_data(path)
    chapters = create_chapters_dicts(data)
    
    target_word = target_word.lower()
    chapters_with_target_word = 0
    total_chapters = len(chapters)

    for chapter in chapters:
        if target_word in chapter:
            chapters_with_target_word += 1

    if total_chapters == 0:
        return 0.0

    chapter_freq = chapters_with_target_word / total_chapters
    return chapter_freq

#Пример использования:

with open("war_peace.txt", "w") as f:
    f.write("[new chapter]\n")
    f.write("привет\n")
    f.write("мир\n")
    f.write("[new chapter]\n")
    f.write("война\n")
    f.write("привет\n")
    f.write("[new chapter]\n")
    f.write("мир\n")


print(chapter_frequency("war_peace.txt", "привет"))
print(chapter_frequency("war_peace.txt", "война"))
print(chapter_frequency("war_peace.txt", "Мир"))


import json
import os

def read_data(path):
    with open(path, 'rt', encoding='windows-1251') as f:
        data = f.read()
    return data.split('\n')

def term_frequency(target_word: str, target_chapter_idx: int) -> float:
    '''
    Напишите программу, которая выведет частоту употребления заданного слова target_word в заданной главе target_chapter.
    tf = количество раз, когда слово target_word встречается в тексте главы / количество всех слов в тексте главы
    '''
    data = read_data("war_peace.txt")
    
    chapter_start = 0
    chapter_end = 0
    chapter_count = 0
    chapter_words = []

    for i, line in enumerate(data):
        if line == "[new chapter]":
            chapter_count += 1
            if chapter_count == target_chapter_idx:
                chapter_start = i + 1
            elif chapter_count > target_chapter_idx:
                chapter_end = i
                break

    if chapter_start == 0:
        return 0.0

    if chapter_end == 0:
        chapter_end = len(data)

    chapter_words = data[chapter_start:chapter_end]
    target_word_count = chapter_words.count(target_word)
    total_words = len(chapter_words)

    if total_words == 0:
        return 0.0

    tf = target_word_count / total_words
    return tf

# Пример использования:
tf = term_frequency("картина", 3)
print(f"Частота слова 'картина' в третьей главе: {tf}")

tf = term_frequency("лес", 5)
print(f"Частота слова 'лес' в пятой главе: {tf}")

tf = term_frequency("несуществующее_слово", 10)
print(f"Частота несуществующего слова в десятой главе: {tf}")

import json
import os

def read_data(path):
    data = open(path, 'rt').read()
    return data.split('\n')

def get_tf_idf(data, target_word: str, target_chapter: int) -> float:
    '''
    Напишите программу, которая выведет значение tf*idf для заданного слова target_word в заданной главе target_chapter.
    https://en.wikipedia.org/wiki/Tf%E2%80%93idf

    tf_idf = tf*idf = term frequency * inverse document frequency
    tf — это частотность термина, которая измеряет, насколько часто термин встречается в документе.
    idf — это обратная документная частотность термина. Она измеряет непосредственно важность термина во всём множестве документов.
    '''

    chapters = []
    current_chapter = []
    for line in data:
        if line == "[new chapter]":
            chapters.append(current_chapter)
            current_chapter = []
        elif line.strip():
            current_chapter.append(line)
    chapters.append(current_chapter)


    if target_chapter >= len(chapters) or target_chapter < 0:
        return 0.0

    target_chapter_data = chapters[target_chapter]
    tf = target_chapter_data.count(target_word)
    
    if tf ==0:
        return 0.0

    total_chapters = len(chapters)
    df = 0
    for chapter in chapters:
        if target_word in chapter:
            df += 1

    if df == 0:
        return 0.0


    idf = 0.0
    if df > 0:
        idf =  total_chapters / df

    tf_idf = (tf / len(target_chapter_data)) * idf if len(target_chapter_data)>0 else 0.0

    return tf_idf

#Пример использования


with open('war_peace.txt', 'w') as f:
    f.write("[new chapter]\n")
    f.write("дом\n")
    f.write("дом\n")
    f.write("карта\n")
    f.write("[new chapter]\n")
    f.write("дом\n")
    f.write("небо\n")
    f.write("[new chapter]\n")
    f.write("карта\n")
    f.write("дом\n")
    f.write("дом\n")
    f.write("дом\n")

data = read_data('war_peace.txt')
target_word = "дом"
target_chapter = 0
result = get_tf_idf(data, target_word, target_chapter)
print(f"TF-IDF для слова '{target_word}' в главе {target_chapter}: {result}")

target_chapter = 2
result = get_tf_idf(data, target_word, target_chapter)
print(f"TF-IDF для слова '{target_word}' в главе {target_chapter}: {result}")

target_word = "небо"
target_chapter = 1
result = get_tf_idf(data, target_word, target_chapter)
print(f"TF-IDF для слова '{target_word}' в главе {target_chapter}: {result}")


