from flask import Flask, render_template
from main import *

app = Flask(__name__)

@app.route('/')
def index():
    mp = read_marketplaces()
    return render_template('marketplaces.html', nome="Marketplaces", marketplace=mp)


@app.route('/categories/<mp>')
def categories(mp):
    cat = read_categories()
    return render_template('categories.html', nome="Categories", categories=cat, mp=mp)


@app.route('/subcategories/<cat>')
def subcategories(cat):
    sub = read_subcategories(cat)
    return render_template('subcategories.html', nome="Subcategories", subcategories=sub, cat=cat)


app.run(debug=True)
