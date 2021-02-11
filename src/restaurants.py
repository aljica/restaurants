from flask import Flask, request, jsonify
from pymongo import MongoClient
from db import DB

app = Flask(__name__)
db = DB('restaurants')

@app.route('/restaurants', methods=['GET'])
def list_restaurants():
    """Get a list of all restaurants."""
    return jsonify(db.get_all_restaurants())

@app.route('/restaurants/<id>', methods=['GET'])
def restaurant_info(id):
    """Get more detailed information on a single restaurant."""
    return jsonify(db.get_restaurant_info(id))

app.run(host='localhost', port=5001)