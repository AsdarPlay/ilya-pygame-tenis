#import sqlite3

#db = sqlite3.connect('maxScore.sqlite')
#cur = db.cursor()

#cur.execute("""
#create table if not exists Records (
    #name text,
    #score integer
#)""")

#cur.execute("""
#SELECT max(score) maxScore from Records
#""")

#result = cur.fetchall()
#print(result)
#cur.close