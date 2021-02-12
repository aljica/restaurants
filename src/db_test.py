import unittest 
import db as Database

class TestDB(unittest.TestCase):


    database = Database.DB('restaurants')


    def test_insert_and_get_info_on_new_restaurant(self):
        test_cases = [
            {
                "data": {
                "opening_hours": ["Monday: 11:00 AM – 3:00 PM","Tuesday: 11:00 AM – 3:00 PM","Wednesday: 11:00 AM – 3:00 PM","Thursday: 11:00 AM – 3:00 PM","Friday: 11:00 AM – 3:00 PM","Saturday: Closed","Sunday: Closed"],
                "name": "John's kitchen",
                "address": "Johngatan 92"
                },
                "expected": "OK"
            },
        ]

        for case in test_cases:
            id = self.database.add_new_restaurants(case['data'])
            
            try:
                id=int(id)
            except ValueError:
                print("Failed integer conversion")
            
            info = self.database.get_restaurant_info(id)
            name = info['name']
            self.assertEqual(name, case['name'])

            #self.assertEqual(id, case['expected'])


if __name__ == "__main__":
    unittest.main()