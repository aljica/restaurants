from flask import Flask, request, jsonify
from pymongo import MongoClient
from db import DB


app = Flask(__name__)
db = DB('restaurants')


@app.route('/restaurants', strict_slashes=False, methods=['GET'])
def list_restaurants():
    """Get a list of all restaurants
    
    Parameters:
    None

    Returns:
    _ (str): Jsonified restaurant data OR
    _ (list): Empty list if no restaurants are in the database.
    """
    return jsonify(db.get_all_restaurants())


@app.route('/restaurants/<id>', strict_slashes=False, methods=['GET'])
def restaurant_info(id):
    """Get more detailed information on a single restaurant
    
    Parameters:
    id (str): Restaurant ID

    Returns:
    _ (str): Jsonified single restaurant data OR
    _ (dict): If integer conversion fails or if restaurant ID is non-existent in the database
    """
    try: id = int(id) 
    except Exception: return {}
    
    return jsonify(db.get_restaurant_info(id))


@app.route('/add_restaurant', strict_slashes=False, methods=['POST'])
def add_restaurant():
    """Add new restaurant to database

    Parameters:
    None 

    Returns:
    _ (str): ID of new restaurant or Exception message
    """

    payload = request.json

    return db.add_new_restaurant(payload)


@app.route('/delete_restaurant/<id>', strict_slashes=False, methods=['POST'])
def delete_restaurant(id):
    """Delete a restaurant from the database

    Parameters:
    id (str): Restaurant ID

    Returns:
    _ (str): OK or Exception message
    """
    try: id = int(id)
    except Exception: return "Failed integer conversion"

    return db.delete_restaurant(id)


if __name__ == "__main__":
    app.run(host='localhost', port=5001)