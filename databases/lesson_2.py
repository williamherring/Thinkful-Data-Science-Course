import sqlite3 as lite

con = lite.connect('getting_started.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT warm_month, AVG(average_high) FROM weather GROUP BY warm_month HAVING AVG(average_high) > 65;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    