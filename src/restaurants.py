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
    try: id = int(id) 
    except Exception: return {}
    
    return jsonify(db.get_restaurant_info(id))


@app.route('/add_restaurant', methods=['POST'])
def add_restaurant():
    """ Test using:
    curl -i -H "Content-Type: application/json" -X POST -d @test.json http://localhost:5001/add_restaurant
    """

    payload = request.json
    data = []
    info_pieces = ['opening_hours', 'address', 'phone_number', 'location', 'icon', 'name', 'price_level', 'rating', 'google_maps_url', 'website', 'photo']
    try:
        for info_piece in info_pieces: data.append(payload[info_piece])
    except KeyError: return "Failed, please supply all data using the correct format."

    return db.add_new_restaurant(data)


if __name__ == "__main__":
    app.run(host='localhost', port=5001)