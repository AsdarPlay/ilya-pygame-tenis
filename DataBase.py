import sqlite3


db = sqlite3.connect('MaxScore.sqlite')
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS MaxScore (
    score INTEGER
)""")
maxScore = c.fetchall()
print(maxScore)

db.commit()
db.close()