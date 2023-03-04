#import sqlite3
#from main import MaxScore

#db = sqlite3.connect('maxScore.sqlite')
#cur = db.cursor()

#cur.execute("""
#create table if not exists Records (
    #score integer
#)""")
#db.commit()
#cur.execute(f"INSERT INTO Records VALUES (?)", (MaxScore))

#cur.execute("""SELECT max(score) maxScore from Records""")

#result = cur.fetchall()
#print(result)
#cur.close