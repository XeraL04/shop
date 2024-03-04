import sqlite3

conn = sqlite3.connect('shop.sqlite')

cursor = conn.cursor()

# cursor.execute('DROP TABLE IF EXISTS products')


cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            desc TEXT
        )
    ''')

conn.commit()

the_products = [
        {"id": 1, "name": "Product 1", "price": 1099, "desc": "Description 1"},
        {"id": 2, "name": "Product 2", "price": 2099, "desc": "Description 2"},
        {"id": 3, "name": "Product 3", "price": 3099, "desc": "Description 3"},
        {"id": 4, "name": "Product 4", "price": 4099, "desc": "Description 4"},
        {"id": 5, "name": "Product 5", "price": 5099, "desc": "Description 5"}
]

cursor.executemany('INSERT INTO products (name, price, desc) VALUES (:name, :price, :desc)', the_products)

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER not null PRIMARY KEY,
                   username TEXT not null,
                   password TEXT not null
)
""")

users = [("userone","password1"),("usertwo2","password"),("userthree","password3")]

cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)


conn.commit()
conn.close()