import nltk
from nltk.collocations import *

file_name = 'blake-poems.txt'
trigram_measures = nltk.collocations.TrigramAssocMeasures()

def get_words(f):
    text=f.read()
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words_without_punctuation  = tokenizer.tokenize(text)
    print(words_without_punctuation)
    return words_without_punctuation

words = get_words(open(file_name,'r'))

finder = BigramCollocationFinder.from_words(words)
word_pair = sorted(finder.nbest(trigram_measures.raw_freq, 1))

print("The most repeated word pair in " +file_name+" : \" " +str (word_pair[0][0]) + " " + str(word_pair[0][1]) + " \"")
