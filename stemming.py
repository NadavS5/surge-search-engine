
from nltk.stem import WordNetLemmatizer

from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize
from functools import reduce
#import nltk
#nltk.download('punkt_tab')
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()
sentence = "Programmers program with programming languages"
while True:

    
    words = sentence.split()
    #print(words)
    #using reduce to apply stemmer to each word and join them back into a string
    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")
    
    lemmetized_sentence = reduce(lambda x, y: x + " " + lemmatizer.lemmatize(y, pos = "n"), words, "")

    print(lemmetized_sentence)
    sentence = input("enter a prompt: ")

#This code is contrinuted by Pushpa.