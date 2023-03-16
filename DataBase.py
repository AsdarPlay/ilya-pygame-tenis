import sqlite3
from main import maxScore

record = maxScore
print(record)
db = sqlite3.connect('MaxScore.sqlite')

c = db.cursor()
#c.execute("""CREATE TABLE MaxScore (
    #score integer
#)""")
c.execute("INSERT INTO MaxScore (record)")

db.commit()
db.close()