import sqlite3

con = sqlite3.connect("db.db")
cur = con.cursor()

res = cur.execute("SELECT user_id FROM users").fetchall()
print(res)