import sqlite3
if __name__ == '__main__':
    #connect to database
    connection = sqlite3.connect('database.db')


    cursor = connection.cursor()


    #cursor.execute('CREATE TABLE IF NOT EXISTS websites (id INTEGER PRIMARY KEY AUTOINCREMENT ,url TEXT UNIQUE, title TEXT, keywords TEXT)')
    #cursor.execute('DELETE FROM websites WHERE 1=1')

    #cursor.execute('CREATE TABLE keywords (id INTEGER PRIMARY KEY AUTOINCREMENT,keyword TEXT NOT NULL UNIQUE')
    #cursor.execute(create_keyword_document_map_quary)


    create_keywords_table_quary =(
        """CREATE TABLE keywords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT NOT NULL UNIQUE
        )""")

    create_keyword_document_map_quary =( 
        """
        CREATE TABLE keyword_website_map (
        keyword_id INTEGER,
        website_id INTEGER,
        relevance_score REAL,
        FOREIGN KEY (keyword_id) REFERENCES keywords(id),
        FOREIGN KEY (website_id) REFERENCES websites(id),
        PRIMARY KEY (keyword_id, website_id))"""
        )#explenation: creates object that keywords stores website's specific keyword evaluation 
        #(FOREIGN KEY (output) REFERENCES table(field)= 
        #stores the primary key of table(field) in output  )

    #cursor.execute(create_keywords_table_quary)
    #cursor.execute(create_keyword_document_map_quary)

    # with open('urls.txt','r') as f:
    #     for line in f.readlines():
    #         cursor.execute('''INSERT INTO websites (url) VALUES (?)''', (line.strip(),))
    connection.commit()
    
    cursor.close()
    connection.close()