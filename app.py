
from flask import Flask, render_template, redirect, Request, request, flash
import psycopg2 

# connecting to an existing database
conn = psycopg2.connect(user="postgres", password="1092", host= "localhost",  port="5432", database="myduka")

# 
cur= conn.cursor()


# create an instance of Flask class/object
app = Flask(__name__)

# @app.route('/', methods= ['POST', 'get'])
# def addproduct():
#     if request.method == "POST":
#         firstname = request.form['fname']
#         lastname = request.form['lname']
#         print(firstname)
#         print(lastname)
#     else:
#         return render_template('posta.html')

# create home route
@app.route('/')
def home():
    return render_template('home.html')

# create inventories route
@app.route('/inventories', methods = ['POST', 'get'])
def inventories():
    if request.method == "POST":

        cur.execute("select * from products")
        data = cur.fetchall()
        for i in data:

         print(i)
    return render_template('inventories.html', datas = data)

# create sales route
@app.route('/sales')
def sales():
    return render_template('sales.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')



# @app.route('/stock')
# def login():
#     return render_template('stock.html')
    




if __name__ == "__main__":
    app.run(debug=True)

 