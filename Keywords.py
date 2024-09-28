import nltk, re
from nltk.stem import WordNetLemmatizer

from urllib.parse import urlparse

class Tokenizer:
    def __init__(self):
        #nltk.download('wordnet')
        #nltk.download('omw-1.4')
        self.lemmatizer = WordNetLemmatizer()

    def __cleanstr(self,text : str):
        pattern = r'[^a-zA-Z0-9\s]'  # Keep only letters, digits, and spaces
        # Replace unwanted symbols with an empty string
        return re.sub(pattern, ' ', text).lower()
    def __tokenize(self,text : str):
        return text.split()
    def __lemmatize_keyword(self,keyword):
        first = self.lemmatizer.lemmatize(keyword,  pos='v')
        return self.lemmatizer.lemmatize(first,  pos='n')
    def do(self,url : str ,text : str):
        clean_text = self.__cleanstr(text)
        text_tokens =self.__tokenize(clean_text)


        return [self.__lemmatize_keyword(keyword) for keyword in text_tokens]
    def do2(self,title : str ,text : str):
        dic = {}


        url_splitted = self.__cleanstr(title).split(" ")
        #url_splitted = url.split(".")

        #url_splitted.pop() # remove the com / net ...

        #print(url_splitted)

        clean_text = self.__cleanstr(text)
        text_tokens =self.__tokenize(clean_text)

        lemmetized_tokens = [self.__lemmatize_keyword(keyword) for keyword in text_tokens + url_splitted ]

        for token in lemmetized_tokens:
            if(token in dic.keys()):
                dic[token] +=1
            else:
                dic[token] =1
        return dic

if(__name__ == "__main__"):
    tokenz = Tokenizer()
    #print(tokenz.do2("google.com","running cats dogs where is my food at smarter ads smart"))
    prompt = input("enter a prompt: ")
    #print(tokenz.do("google.com",prompt))
    print(tokenz.do2("google.com",prompt))
