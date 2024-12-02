# Task 2. 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

def is_prefix_of_word(sentence, searchWord):
    # Split the sentence into words
    words = sentence.split()

    # Loop through each word in the sentence
    for i in range(len(words)):
        # Check if searchWord is a prefix of the current word
        if words[i].startswith(searchWord):
            # Return the 1-indexed position
            return i + 1

    # If no word matches, return -1
    return -1


# Example usage
sentence = "i love eating burger"
searchWord = "burg"
print(is_prefix_of_word(sentence, searchWord))  # Output: 4