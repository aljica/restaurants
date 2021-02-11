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
            id = restaurant['id']
            name = restaurant['name']
            opening_hours = restaurant['opening_hours']
            address = restaurant['address']
            
            info.append({'id': id, 'name': name, 'opening_hours': opening_hours, 'address': address})
        return info

    
    def add_new_restaurant(self):
        pass

    
    def insert_restaurant(self, data):
        pass


def main():
    db = DB('restaurants')
    restaurant_names = db.get_all_restaurants()
    print(restaurant_names)


if __name__ == "__main__":
    main()
    #pass