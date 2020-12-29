from flask import Flask, render_template
from log import *
from historic import *

app = Flask(__name__)


@app.route('/')
def index():
    mp = read_column("Marketplace")
    save_log("WEB: List of Marketplaces visualized")
    return render_template('marketplaces.html', nome="Marketplaces", marketplace=mp)


@app.route('/categories/<mp>')
def categories(mp):
    cat = read_categories(mp)
    save_log(f"WEB: Categories for {mp} visualized: {cat}")
    return render_template('categories.html', nome="Categories", categories=cat, mp=mp)


@app.route('/subcategories/<cat>/<mp>')
def subcategories(cat, mp):
    sub = read_subcategories(mp, cat)
    save_log(f"WEB: Subcategories of {cat} opened for {mp} visualized: {sub}")
    return render_template('subcategories.html', nome="Subcategories", subcategories=sub, cat=cat)


app.run(debug=True)
