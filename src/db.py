from pymongo import MongoClient 

class DB:
    """
    A class used to represent a database.

    Attributes
    ----------
    db (Database Object): 
        MongoClient Database Object
    
    collection (Collection Object): 
        MongoClient Collection Object

    Methods
    -------
    get_all_restaurants(): 
        Returns a list of all restaurants in the database.

    get_restaurant_info(id): 
        Returns detailed information on a single specified (by id) restaurant.

    add_new_restaurant(data):
        Adds a new restaurant with the information provided in parameter `data` to the database.

    delete_restaurant(id):
        Deletes a restaurant from the database.
    """

    def __init__(self, collection_name = ""):
        """Database initilization

        Parameters:
        collection_name = ""

        Returns:
        None
        """
        try:
            client = MongoClient()
            self.db = client.viaplay
            self.collection = self.db[collection_name] # Contains all database information.
        except Exception as e:
            print(e)

    
    def get_all_restaurants(self):
        """Get all restaurants in database

        Parameters:
        None 

        Returns:
        List of restaurant id:s and names
        """
        restaurant_names = []
        for restaurant in self.collection.find():
            id = restaurant['id']
            name = restaurant['name']
            restaurant_names.append({'id': id, 'name': name})
        return restaurant_names

    
    def get_restaurant_info(self, id):
        """Get information on a specific restaurant

        Parameters:
        id (int): Restaurant ID

        Returns:
        info (list): Detailed restaurant information
        """
        info = []
        for restaurant in self.collection.find({"id": id}):
            try:
                info.append({'id': restaurant['id'], 'name': restaurant['name'], 'opening_hours': restaurant['opening_hours'], 'address': restaurant['address']})
            except KeyError: return {}
        
        return info

    
    def add_new_restaurant(self, data):
        """Add new restaurant to the database

        Parameters:
        data (list): List containing information on the new restaurant to be added

        Returns:
        _ (str): OK or Exception message
        """
        id = -1
        try:
            # First, get the ID of the most recently inserted restaurant (so we know which ID the new one should have)
            # What will happen if there are no restaurants in the DB? Will exception be raised? In that case, deleting everything from the DB will cause a bug. Must be tested.
            latest_restaurant = self.collection.find({}).sort('id', -1).limit(1)
            if latest_restaurant.alive:
                # If the latest restaurant entry was found
                for doc in latest_restaurant: 
                    id = doc['id'] + 1
            else:
                # No entries in the database, so id should be 0.
                id = 0
        except Exception: return "Failed during ID creation"

        try:
            self.collection.insert_one({'opening_hours': data[0], 'address': data[1], 'phone_number': data[2], 'location': data[3], 'icon': data[4], 'name': data[5], 'price_level': data[6], 'rating': data[7], 'google_maps_url': data[8], 'website': data[9], 'photo': data[10], 'id': id})
            return "OK"
        except Exception: return "Failed during data insertion, double-check the format of your inputs"


    def delete_restaurant(self, id):
        """Delete a restaurant from the database.

        Parameters:
        id (int): Restaurant id

        Returns:
        _ (str): OK or Exception message
        """
        try: 
            self.collection.delete_one({'id': id})
            return "OK"
        except Exception: return "Failed during deletion"


def main():
    db = DB('restaurants')
    restaurant_names = db.get_all_restaurants()


if __name__ == "__main__":
    main()