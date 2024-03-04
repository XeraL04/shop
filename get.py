import sqlite3 

conn = sqlite3.connect("shop.sqlite")

cursor = conn.cursor()

cursor.execute("SELECT * FROM products")
# cursor.execute("SELECT * FROM users")

data = cursor.fetchall()

print(data)

conn.close()