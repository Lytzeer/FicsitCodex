from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, jsonify
from Funcs.items_getters import get_items, get_item_by_id, get_item_all_primary_info
from Funcs.recipes_getters import get_recipes
from Funcs.schematics_getters import get_schematics
from Funcs.generators_getters import get_generators
from Funcs.resources_getters import get_resources
from Funcs.miners_getters import get_miners
from Funcs.buildings_getters import get_buildings

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

API_HOST = environ.get('API_HOST')
API_PORT = environ.get('API_PORT')

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Project Ficsit Codex'})

@app.route('/items')
@app.route('/items/')
def items():
    return get_items()

@app.route('/items/<string:id>')
@app.route('/items/<string:id>/')
def item_by_id(id):
    return get_item_by_id(id)

@app.route('/items/<string:id>/primary')
@app.route('/items/<string:id>/primary/')
def item_primary_info(id):
    return get_item_all_primary_info(id)

@app.route('/recipes')
def recipes():
    return get_recipes()

@app.route('/schematics')
def schematics():
    return get_schematics()

@app.route('/generators')
def generators():
    return get_generators()

@app.route('/resources')
def resources():
    return get_resources()

@app.route('/miners')
def miners():
    return get_miners()

@app.route('/buildings')
def buildings():
    return get_buildings()

if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT)