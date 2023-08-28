from flask import Flask, Blueprint, render_template
from poke_api import item_list
app = Flask(__name__)
app.debug = True

@app.route('/')
@app.route('/home')
def home():
    sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/'
    return render_template('index.html', sprite = sprite, item_list = item_list, grid_count = 0)
