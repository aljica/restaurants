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

    get_info(restaurant):
        Extract the necessary information from a restaurant mongoDB collection or dictionary containing information on a restaurant.

    get_restaurant_info(id): 
        Returns detailed information on a single specified (by id) restaurant.

    create_new_id():
        Creates new restaurant ID.

    add_new_restaurants(restaurants):
        Adds new restaurants with the information provided in parameter `restaurants` to the database.

    delete_restaurant(id):
        Deletes a restaurant from the database.

    delete_restaurants(ids):
        Deletes multiple restaurants from the database.
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
        restaurants (list): List of restaurant id:s and names
        """
        restaurants = []
        for restaurant in self.collection.find():
            try:
                id = restaurant['id']
                name = restaurant['name']
            except KeyError: 
                return "Internal DB error, looks like some restaurants don't have ID and/or name."
            restaurants.append({'id': id, 'name': name})
        return restaurants

    
    def get_info(self, restaurant):
        """Extract the necessary information from a restaurant mongoDB collection.

        Parameters:
        restaurant (pymongo.Collection): A restaurant collection object OR
        restaurant (dict): Dictionary containing information on a restaurant

        Returns:
        info (dict): Information extracted from collection object (opening_hours, address, name etc) OR
        _ (str): Exception message
        """
        INFO_PIECES = ['opening_hours', 'address', 'phone_number', 'location', 'icon', 'name', 'price_level', 'rating', 'google_maps_url', 'website', 'photo', 'description']
        MUST_HAVES = ['opening_hours', 'address', 'name']

        info = {}
        for info_piece in INFO_PIECES:
            try:
                info[info_piece] = restaurant[info_piece]
            except KeyError:
                if info_piece in MUST_HAVES:
                    return "Missing must_have info_piece"
                else:
                    continue
        return info


    def get_restaurant_info(self, id):
        """Get information on a specific restaurant

        Parameters:
        id (int): Restaurant ID

        Returns:
        info (list): Detailed restaurant information OR empty dict if restaurant ID is non-existent OR Exception message
        """
        info = {}
        for restaurant in self.collection.find({"id": id}): 
            info = self.get_info(restaurant)
        return info


    def create_new_id(self):
        """Creates new restaurant ID

        Parameters:
        None

        Returns:
        id (int): Restaurant ID
        """
        id = 0
        try:
            latest_restaurant = self.collection.find({}).sort('id', -1).limit(1)
            if latest_restaurant.alive:
                # If the restaurant with highest id was found
                for doc in latest_restaurant: 
                    id = doc['id'] + 1
        except Exception: pass
        return id


    def add_new_restaurants(self, restaurants):
        """Add new restaurants to the database

        Parameters:
        data (dict): Dict containing information on the new restaurants to be added

        Returns:
        _ (str): Dictionary with 1 element ('ids') mapped to a list containing all the ID's of the newly created restaurants (problem with returning lists with Flask, so we return a dictionary instead)
        """
        ids = {'ids': []}
        # Create new ID
        for restaurant in restaurants:
            id = self.create_new_id()
            info = self.get_info(restaurant)
            if not isinstance(info, dict):
                # This means an error was raised, i.e. a must_have info_piece was missing from the json data.
                print("Must_have info_piece missing, skipping.") 
                continue
            info['id'] = id
            
            # Insert into DB
            try:
                self.collection.insert_one(info)
                ids['ids'].append(id)
            except Exception: return "Failed during data insertion, double-check the format of your inputs"
        
        return ids


    def delete_restaurant(self, id):
        """Delete a restaurant from the database

        Parameters:
        id (int): Restaurant id

        Returns:
        _ (str): OK or Exception message
        """
        try: 
            result = self.collection.delete_one({'id': id})
            return "OK"
        except Exception: return "Failed during deletion"
    
   
    def delete_restaurants(self, ids):
        """Delete multiple restaurants from the database

        Parameters:
        ids (list): List of restaurant IDs

        Returns:
        _ (str): OK or Exception message
        """
        for id in ids:
            result = self.delete_restaurant(id)
            if result != "OK":
                print(result)
                print("Continuing")
                continue
        return "OK"