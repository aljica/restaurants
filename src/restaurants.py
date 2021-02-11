from flask import Flask, request, jsonify
from pymongo import MongoClient
from db import DB

app = Flask(__name__)
db = DB('restaurants')

@app.route('/restaurants', methods=['GET'])
def home():
    return jsonify(db.get_all_restaurants())

app.run(host='localhost', port=5001)