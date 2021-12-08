from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/about')
def hey():
    #return "my first function in Web curse"
    return redirect(url_for('s_func'))

@app.route('/loginPag')
def s_func():
    return "this is login page"

@app.route('/product')
@app.route('/products')
def get_products():
    return "hello products"

@app.route('/')
def home():
   # return "home page"
    return redirect('/products')

if __name__=='__main__':
    app.run(debug=True)


