import sqlite3

#connect to database
connection = sqlite3.connect('database.db')


cursor = connection.cursor()


#cursor.execute('CREATE TABLE IF NOT EXISTS websites (url TEXT UNIQUE, title TEXT, keywords TEXT)')
cursor.execute('DELETE FROM websites WHERE 1=1')

#cursor.execute('CREATE TABLE keywords (id INTEGER PRIMARY KEY AUTOINCREMENT,keyword TEXT NOT NULL UNIQUE')
#cursor.execute(create_keyword_document_map_quary)

create_keyword_document_map_quary =( 
    """
    CREATE TABLE keyword_document_map (
    keyword_id INTEGER,
    document_id INTEGER,
    relevance_score REAL,
    FOREIGN KEY (keyword_id) REFERENCES keywords(id),
    FOREIGN KEY (document_id) REFERENCES documents(id),
    PRIMARY KEY (keyword_id, document_id)"""
    )#explenation: creates object that keywords stores website's specific keyword evaluation 
    #(FOREIGN KEY (output) REFERENCES table(field)= 
    #stores the primary key of table(field) in output  )



# with open('urls.txt','r') as f:
#     for line in f.readlines():
#         cursor.execute('''INSERT INTO websites (url) VALUES (?)''', (line.strip(),))
connection.commit()

cursor.close()
connection.close()