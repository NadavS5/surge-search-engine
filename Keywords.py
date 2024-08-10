from nltk.stem import WordNetLemmatizer
import nltk, re
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
        return self.lemmatizer.lemmatize(keyword,  pos='v')
    def do(self,text : str):
        clean_text = self.__cleanstr(text)
        text_tokens =self.__tokenize(clean_text)


        return [self.__lemmatize_keyword(keyword) for keyword in text_tokens]
    def do2(self,text : str):
        dic = {}
        clean_text = self.__cleanstr(text)
        text_tokens =self.__tokenize(clean_text)

        lemmetized_tokens = [self.__lemmatize_keyword(keyword) for keyword in text_tokens]

        for token in lemmetized_tokens:
            if(token in dic. keys()):
                dic[token] +=1
            else:
                dic[token] =1
        return dic

if(__name__ == "__main__"):
    tokenz = Tokenizer()
    print(tokenz.do("running cats dogs where is my food at"))
    prompt = input("enter a prompt: ")
    print(tokenz.do(prompt))
    print(tokenz.do2(prompt))