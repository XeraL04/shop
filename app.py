from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

def get_users():
    con = sqlite3.connect('shop.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    con.close()

    return users

def get_data():
    con = sqlite3.connect('shop.sqlite')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    cursor.execute("SELECT * FROM products")
    data = [dict(row) for row in cursor.fetchall()]

    cursor.close()
    con.close()

    return data

@app.route("/")
def index():
    if 'username' in session:
        products = get_data()
        return render_template('index.html', products=products, username=session['username'])
    else:
        flash('You need to log in to view the products. Please log in.')
        return redirect(url_for('add_post_form'))

@app.route("/sign_in_form")
def add_post_form():
    return render_template('signin.html')

@app.route("/sign_in", methods=["POST"])
def signin():
    if request.method == "POST":
        username = request.form["new_user"]
        password = request.form["new_password"]

        con = sqlite3.connect("shop.sqlite")
        cursor = con.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        cursor.close()
        con.close()

        if user:
            session['username'] = username
            flash('Logged in successfully!')
            return redirect(url_for("index"))
        else:
            flash('Invalid credentials. Please try again.')

    return redirect(url_for("add_post_form"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    products = get_data()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        flash('Product not found', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(__name__)

# def get_users():
#     con = sqlite3.connect('shop.sqlite')
#     cursor = con.cursor()
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     cursor.close()
#     con.close()

#     return users

# def get_data():
#     con = sqlite3.connect('shop.sqlite')

#     con.row_factory = sqlite3.Row

#     cursor = con.cursor()

#     cursor.execute("SELECT * FROM products")

#     # data = cursor.fetchall()
#     data = [dict(row) for row in cursor.fetchall()]

#     cursor.close()
#     con.close()

#     return data

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/sign_in_form")
# def add_post_form():
#     return render_template('signin.html')

# @app.route("/sign_in", methods=["POST"])
# def signin():
#     if request.method == "POST":
#         new_user = request.form["new_user"]
#         new_password = request.form["new_password"]
#         con = sqlite3.connect("shop.sqlite")
#         cursor = con.cursor()
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_user, new_password))
#         con.commit()
#         con.close()

#         return redirect(url_for("index"))

# @app.route('/product/<int:product_id>')
# def product_detail(product_id):
#     products = get_data()
#     product = next((p for p in products if p['id'] == product_id), None)
#     if product:
#         return render_template('product_detail.html', product=product)
#     else:
#         return "Product not found", 404
    

# if __name__ == '__main__':
#     app.run(debug=True)