from flask import Flask, render_template
from main import *

app = Flask(__name__)

back = "<br><br><a href='/'>Go back</a>"


@app.route('/')
def index():
    text = "<h1>Marketplaces</h1>"
    mp = read_marketplaces()
    for i in mp:
        text += "<br><a href='/categories'>" + i + "</a>"
    return text + back


@app.route('/categories')
def categories():
    text = "<h1>Categories</h1>"
    cat = read_categories()
    for i in cat:
        text += "<br><a href='/subcategories/" + i + "'>" + i + "</a>"
    return text + back


@app.route('/subcategories/<cat>')
def subcategories(cat):
    text = "<h1>Subcategories for " + cat + "</h1>"
    sub = read_subcategories(cat)
    for i in sub:
        text += "<br>" + i
    return text + back


app.run()
