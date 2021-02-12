from pymongo import MongoClient 


INFO_PIECES = ['opening_hours', 'address', 'phone_number', 'location', 'icon', 'name', 'price_level', 'rating', 'google_maps_url', 'website', 'photo']
MUST_HAVES = ['opening_hours', 'address', 'name']


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
            try:
                id = restaurant['id']
                name = restaurant['name']
            except KeyError: return "Internal DB error, looks like some restaurants don't have ID and/or name."
            restaurant_names.append({'id': id, 'name': name})
        return restaurant_names

    
    def get_restaurant_info(self, id):
        """Get information on a specific restaurant

        Parameters:
        id (int): Restaurant ID

        Returns:
        info (list): Detailed restaurant information OR {} if restaurant ID is non-existent
        """
        info = {}
        for restaurant in self.collection.find({"id": id}):
            try:
                for info_piece in MUST_HAVES:
                    info[info_piece] = restaurant[info_piece]
            except KeyError: return {}
        return info

    
    def add_new_restaurant(self, data):
        """Add new restaurant to the database

        Parameters:
        data (dict): Dict containing information on the new restaurant to be added

        Returns:
        _ (str): ID of new restaurant or Exception message
        """
        insert_data = {}
        id = 0
        try:
            latest_restaurant = self.collection.find({}).sort('id', -1).limit(1)
            if latest_restaurant.alive:
                # If the latest restaurant entry was found
                for doc in latest_restaurant: 
                    id = doc['id'] + 1
        except Exception: return "Failed during ID creation"
        insert_data['id'] = id

        for info_piece in INFO_PIECES:
            try:
                insert_data[info_piece] = data[info_piece]
            except KeyError:
                if info_piece in MUST_HAVES:
                    return "Failed during data retrieval from your .json file, please double-check the format of your inputs. Must haves are opening_hours, address and name."
                else:
                    continue
        
        try:
            self.collection.insert_one(insert_data)
            return str(id)
        except Exception: return "Failed during data insertion, double-check the format of your inputs"


    def delete_restaurant(self, id):
        """Delete a restaurant from the database.

        Parameters:
        id (int): Restaurant id

        Returns:
        _ (str): OK or Exception message
        """
        try: 
            result = self.collection.delete_one({'id': id})
            return "OK"
        except Exception: return "Failed during deletion"


#def main():
#    db = DB('viaplay')


#if __name__ == "__main__":
#    main()