import sqlite3
from Keywords import Tokenizer
import numpy as np

class Database:
    def __init__(self):
        self.__sqliteConnection = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.__sqliteConnection.cursor()
    def __del__(self):
        self.__sqliteConnection.close()
    def addWebsite(self, url:str, title :str, keywords: dict[str,str] ):

        ##tf##
        term_count = sum(keywords.values())
        print(term_count)
        ##tf##

        print('website')
        self.cursor.execute('''INSERT INTO websites (url,title) VALUES (?,?)''', (url.strip(),title.strip()))
        website_id = self.cursor.lastrowid
        for keyword, times in keywords.items():

            tf =  times/term_count

            self.cursor.execute('''INSERT OR IGNORE INTO keywords (keyword,count) VALUES (?,?)''', ((keyword,0)))
            
            self.cursor.execute('''SELECT id , count FROM keywords WHERE keyword = ?''', (keyword,))

            result = self.cursor.fetchall()[0]
            keyword_id = result[0]
            #document_frequency = result[1]

            self.cursor.execute('''UPDATE keywords SET count = count + 1 WHERE id = ?''',((keyword_id,)))

            
            #print(keyword , term_count , times , tf)
            self.cursor.execute('''INSERT INTO keyword_website_map (keyword_id,website_id,tf) VALUES (?,?,?)''',
                (keyword_id, website_id, tf)
            )
        self.__sqliteConnection.commit()

    # main search function
    def search(self,keywords: dict[str,str] ):

        results = {}

        for keyword, times in keywords.items():
            self.cursor.execute(f'''

                SELECT d.url, d.title, kwm.tf
                FROM keyword_website_map kwm
                JOIN keywords k ON kwm.keyword_id = k.id
                JOIN websites d ON kwm.website_id = d.id
                WHERE k.keyword = '{keyword}'
                ORDER BY kwm.tf DESC;
                ''')
            result = self.cursor.fetchall()

            for url ,title , tf in result:
                if(url in results.keys()):
                    results[url] +=tf
                else:
                    results[url] =tf
        vals =  list(results.values())
        sorted_vals = np.argsort(vals)[::-1]


            #print(list(results.values()))
            
        keys = list(results.keys())
        sorted_results = {keys[i] : vals[i] for i in sorted_vals}
        #print(sorted_results)
        return sorted_results



if __name__ == '__main__':
    print('main')
    db = Database()
    #db.addWebsite("google.com","google",{'google':3})
    
    tk = Tokenizer()
    #db.search({'google':1})
    #db.addWebsite('marclou.com', 'Marc lou', tk.do2('marc lou' , 'solopreneurs read Just Ship It'))
    db.search(tk.do2("", input("enter your search: ")))
    #db.addWebsite('google.com', 'Google', tk.do2('google ' , 'google search engine'))
    
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google search engine'))
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google search engine'))
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google google google search engine'))
    #print(tk.do2('google.com' , 'google google google search engine'))