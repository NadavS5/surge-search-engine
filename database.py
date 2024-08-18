import sqlite3
from Keywords import Tokenizer
class Database:
    def __init__(self):
        self.__sqliteConnection = sqlite3.connect('database.db')
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




if __name__ == '__main__':
    print('main')
    db = Database()
    #db.addWebsite("google.com","google",{'google':3})
    
    tk = Tokenizer()


    db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google search engine'))
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google search engine'))
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google search engine'))
    #db.addWebsite('google.com', 'Google', tk.do2('google.com' , 'google google google search engine'))
    #print(tk.do2('google.com' , 'google google google search engine'))