# regex for removing punctuation!
import re
# nltk preprocessing magic
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# grabbing a part of speech function:
from part_of_speech import get_part_of_speech

from nltk.tokenize import word_tokenize

text = "So many squids are jumping out of suitcases these days that you can barely go anywhere without seeing one burst forth from a tightly packed valise. I went to the dentist the other day, and sure enough I saw an angry one jump out of my dentist's bag within minutes of arriving. She hardly even noticed."

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

stemmer = PorterStemmer()
stemmed = [stemmer.stem(token) for token in tokenized]


# Define a WordNetLemmatizer instance
lemmatizer = WordNetLemmatizer()

# Define the text to tokenize and lemmatize
text = "I went to the store and bought some apples. Then I decided to go home."

# Tokenize the text into a list of words
tokenized = word_tokenize(text)

# Lemmatize each word in the list
lemmatized = [lemmatizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized]
# Print the original and lemmatized lists
print("Original tokens:", tokenized)
print("Lemmatized tokens:", lemmatized)
print("Stemmed text:")
print(stemmed)
print("\nLemmatized text:")
print(lemmatized)