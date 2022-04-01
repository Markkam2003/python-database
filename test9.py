
import sqlite3


fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

textList = []


#  Create database and table 
conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_misc(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        files VARCHAR(255))")
    conn.commit



# Query .txt filenames
def getTextFile():
    for f in fileList:
        if f.endswith(".txt"):
            textList.append(f)
        
getTextFile()



# Insert .txt filenames into table
def dataEntry():
    for i in textList:
        cur.execute("INSERT INTO tbl_misc(files) VALUES(?)", (i,))
        conn.commit

dataEntry()



# Query database and print to console
with conn:
    cur.execute("SELECT * FROM tbl_misc")
    rows = cur.fetchall()
    for row in rows:
        msg = "File ID: {}, File Name: {}".format(row[0],row[1])
        print(msg)
    
