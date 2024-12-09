import os
import json

def read_data(path):
    """
    Reads the text file and returns its content as a list of lines.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def word_dictionary(data):
    """
    Creates a word frequency dictionary from the given data.
    
    Args:
        data (list): List of words.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    frequency_dict = {}
    for word in data:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return frequency_dict

def create_chapters_dicts(data):
    """
    Creates a list of word frequency dictionaries, one for each chapter.

    Args:
        data (list): List of words with chapter delimiters `[new chapter]`.

    Returns:
        list: A list of dictionaries, each representing word frequencies for a chapter.
    """
    chapter_indices = [i for i, line in enumerate(data) if line == '[new chapter]']
    chapters = []
    start = 0

    for index in chapter_indices:
        chapter_content = data[start:index]
        chapter_frequency = word_dictionary(chapter_content)
        chapters.append(chapter_frequency)
        start = index + 1

    # Add the last chapter
    last_chapter = data[start:]
    chapters.append(word_dictionary(last_chapter))
    return chapters

def chapter_frequency(path, target_word):
    """
    Calculates the chapter frequency of a target word.

    Args:
        path (str): Path to the text file.
        target_word (str): The target word to analyze.

    Returns:
        float: The chapter frequency.
    """
    data = read_data(path)
    chapter_frequencies = create_chapters_dicts(data)
    num_chapters_with_word = sum(1 for chapter in chapter_frequencies if target_word in chapter)
    total_chapters = len(chapter_frequencies)
    return num_chapters_with_word / total_chapters if total_chapters > 0 else 0

def term_frequency(target_word, target_chapter_idx, chapter_frequencies):
    """
    Calculates the term frequency of a word in a specific chapter.

    Args:
        target_word (str): The target word to analyze.
        target_chapter_idx (int): Index of the target chapter.
        chapter_frequencies (list): List of chapter word frequency dictionaries.

    Returns:
        float: The term frequency.
    """
    if target_chapter_idx >= len(chapter_frequencies):
        raise ValueError("Invalid chapter index.")
    
    chapter = chapter_frequencies[target_chapter_idx]
    total_words = sum(chapter.values())
    return chapter.get(target_word, 0) / total_words if total_words > 0 else 0

def inverse_document_frequency(data, target_word):
    """
    Calculates the inverse document frequency of a word across all chapters.

    Args:
        data (list): List of words with chapter delimiters `[new chapter]`.
        target_word (str): The target word to analyze.

    Returns:
        float: The inverse document frequency.
    """
    chapter_frequencies = create_chapters_dicts(data)
    num_chapters_with_word = sum(1 for chapter in chapter_frequencies if target_word in chapter)
    total_chapters = len(chapter_frequencies)
    import math
    return math.log((total_chapters / (1 + num_chapters_with_word))) if num_chapters_with_word > 0 else 0

def get_tf_idf(path, target_word, target_chapter_idx):
    """
    Calculates the TF-IDF value for a word in a specific chapter.

    Args:
        path (str): Path to the text file.
        target_word (str): The target word to analyze.
        target_chapter_idx (int): Index of the target chapter.

    Returns:
        float: The TF-IDF value.
    """
    data = read_data(path)
    chapter_frequencies = create_chapters_dicts(data)
    tf = term_frequency(target_word, target_chapter_idx, chapter_frequencies)
    idf = inverse_document_frequency(data, target_word)
    return tf * idf

# Example usage
if __name__ == "__main__":
    # Ensure you provide the correct path to "war_peace.txt"
    file_path = "war_peace.txt"
    
    # Word analysis
    target_word = "war"
    target_chapter = 2  # Example chapter index

    # Read and process data
    print("Chapter Frequency:", chapter_frequency(file_path, target_word))
    print("TF-IDF:", get_tf_idf(file_path, target_word, target_chapter))
