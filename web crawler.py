import re
import queue
import threading
import sqlite3
import requests
from urllib.parse import urlparse
from html.parser import HTMLParser
from Keywords import Tokenizer
from database import Database

sqliteConnection = sqlite3.connect('database.db')
cursor = sqliteConnection.cursor()


root = "google.com"

url_queue = queue.Queue()
url_done = set() 

db = Database()
tokenizer = Tokenizer()


def readqueue(queue  , fname ):
    with open(fname , 'r')as f :
        for line in f.readlines():
            queue.put(line.strip())

def readdone(done  , fname ):
    with open(fname , 'r')as f :
        for line in f.readlines():
            done.add(line.strip())

class MyParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.tag_data = []
        self.counter = 0
        self.istitle = False
        self.ish1 = False
        self.title = ""
        self.h1 = ""
        self.description = ""
        
        
        self.save_tags = ["h1", "h2", "h3", "title", "meta" , "a"]
    def scrap(self, data, file):
        self.feed(data)
        
    def handle_starttag(self,tag ,attrs):
        if(tag in self.save_tags) :
            if(tag == 'title'):
                
                self.istitle = True
            if(tag == 'meta'):
                #print(list(attrs))
                if(attrs[0][1] == "og:description" or attrs[0][1] == "twitter:description"):
                    if(attrs[1][0] == 'content'):
                        self.description = attrs[1][1]



            if(tag == 'h1' or tag =='h2' or tag =='h3'):
                self.ish1 = True

            for attr in attrs:
                if (attr[0] == 'href'):

                    if(isinstance(attr[1], str) and  attr[1].startswith("https://")):

                        url = urlparse(attr[1]).netloc.replace('www.', '')
                        
                        if(url in url_done):
                            break
                        
                           
                        url_queue.put(url)
                        url_done.add(url)

                        f.write(url  + "\n")

                        self.counter +=1
                
            #if(attr[0] == 'property'):
    def handle_data(self, data):
        if(self.istitle ==True):
            self.title = data
            self.istitle = False
        if(self.ish1 ==True):
            self.h1 +=" "+data 
            self.ish1 = False

# p = HTMLParser()
parser =  MyParser()
# url_queue.append(root)
# url_done.append(root)

readqueue(url_queue, 'queue.txt')

readdone(url_done, 'queue.txt')
readdone(url_done,'urls.txt')

headers = {"Accept-Language": "en-US,en;q=0.5"}

with open("urls.txt", "a") as f:
 
    
    
    while(url_queue.qsize() > 0) :
        
        url = url_queue.get()

        

        # print("done", parser.counter)
        # print("in queue",   url_queue.qsize())
        # print("current", url)

        try:
            parser.scrap(requests.get("https://"  + url,headers = headers,  timeout = 5).text, f)
            #print(url.strip(),parser.title.strip(), tokenizer.do( parser.description +" "+ parser.title) )
            #enter url and title to database

            
            #keywords_array = tokenizer.do( parser.title , parser.description)
            keywords_dict = tokenizer.do2( parser.title , parser.description)
            #convert array to string with join()
            #keywords = " ".join(keywords_array)
            #print(keywords)

            db.addWebsite(url.strip(), parser.title.strip(), keywords_dict)

            #cursor.execute('''INSERT INTO websites (url,title,keywords) VALUES (?,?,?)''', (url.strip(),parser.title.strip(), keywords))
           # sqliteConnection.commit()
            #print(url.strip(),parser.title.strip())
        except Exception as e:
           print("error" )
           print (e)
        except KeyboardInterrupt :
            print("done")
            break
        


with open("queue.txt", 'w')as f :
    #f.writelines(url + "\n" for url in url_queue)
    while(url_queue.qsize()> 0):
        f.write(url_queue.get()  +  "\n")
#print(parser.scrap(requests.get(root).text))
#print(requests.get(root).text)
sqliteConnection.close()