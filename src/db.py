from pymongo import MongoClient 

class DB:
    def __init__(self, collection_name = ""):
        # Database initialization
        try:
            client = MongoClient()
            self.db = client.viaplay
            self.collection = self.db[collection_name] # Contains all database information.
        except Exception as e:
            print(e)

    
    def get_all_restaurants(self):
        restaurant_names = []
        for restaurant in self.collection.find():
            id = restaurant['id']
            name = restaurant['name']
            restaurant_names.append({'id': id, 'name': name})
        return restaurant_names

    
    def get_restaurant_info(self, id):
        info = []
        for restaurant in self.collection.find({"id": id}):
            try:
                info.append({'id': restaurant['id'], 'name': restaurant['name'], 'opening_hours': restaurant['opening_hours'], 'address': restaurant['address']})
            except KeyError: return {}
        
        return info

    
    def add_new_restaurant(self, data):
        id = -1
        try:
            # First, get the ID of the most recently inserted restaurant (so we know which ID the new one should have)
            # What will happen if there are no restaurants in the DB? Will exception be raised? In that case, deleting everything from the DB will cause a bug. Must be tested.
            latest_restaurant = self.collection.find({}).sort('id', -1).limit(1)
            for doc in latest_restaurant: id = doc['id'] + 1
        except Exception: 
            print("FAILED FIRST")
            return "Failed during ID creation"

        try:
            self.collection.insert_one({'opening_hours': data[0], 'address': data[1], 'phone_number': data[2], 'location': data[3], 'icon': data[4], 'name': data[5], 'price_level': data[6], 'rating': data[7], 'google_maps_url': data[8], 'website': data[9], 'photo': data[10], 'id': id})
            return "OK"
        except Exception:
            print("FAILED")
            return "Failed during data insertion, double-check the format of your inputs"


def main():
    db = DB('restaurants')
    restaurant_names = db.get_all_restaurants()
    print(restaurant_names)


if __name__ == "__main__":
    main()
    #pass