from typing import List, Union
import requests
from bs4 import BeautifulSoup

def get_wiki_info(keyword: str, max_num_sentences: int = 10, max_sentence_length: int = 10) -> Union[List[str], None]:
    url = f"https://simple.wikipedia.org/wiki/{keyword}"
    try:
        # Request the webpage
        response = requests.get(url)
        if response.status_code != 200:
            return []

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')  # Extract paragraphs

        sentences = []

        # Iterate over the paragraphs
        for paragraph in paragraphs:
            text = paragraph.get_text()
            for sentence in text.split('.'):  # Split paragraph into sentences
                stripped_sentence = sentence.strip()
                if stripped_sentence.lower().startswith(keyword.lower()):
                    # Split the sentence into words and truncate if necessary
                    words = stripped_sentence.split()
                    if len(words) > max_sentence_length:
                        stripped_sentence = ' '.join(words[:max_sentence_length])
                    sentences.append(stripped_sentence)
                    # Stop if we've reached the max number of sentences
                    if len(sentences) >= max_num_sentences:
                        return sentences

        return sentences
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


# Usage example
print(get_wiki_info("Neurolinguistic programming", max_num_sentences=2, max_sentence_length=4))
