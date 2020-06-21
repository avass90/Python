import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png'\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('step162.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    conn.commit()
conn.close()
        

for item in fileList:
    if item.endswith('.txt'):
    
        conn = sqlite3.connect('step162.db')
                                        
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_fname) VALUES (?)",\
                (item,))
            conn.commit()
        conn.close()
        print(item)
