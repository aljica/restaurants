# Restaurants

This repository contains an implementation of a REST API that can read and write into the provided db while providing endpoints to clients from which they will be able to perform basic CRUD (Create, Read, Update, Delete) operations on the database. 

## Prerequisites

* Python3
* [MongoDB](https://www.mongodb.com/)

**Libraries**

* Python Standard Library >= 3.8.5
* [Flask](https://pypi.org/project/Flask/)
* [pymongo](https://pypi.org/project/pymongo/)

**Optional**

* [Ngrok](https://ngrok.com/)

## Installation & Usage Instructions

Install Python3, MongoDB and the required libraries. <br>
Ubuntu/Debian: <br>
`sudo apt install python3` <br>
`sudo apt install mongodb` <br>
`sudo apt install python3-pip` <br>
`pip3 install -r requirements.txt` (This will install flask and pymongo - it is advisable that you run this command inside the virtual environment, see below)

Setup Python3 virtual environment: <br>
`python3 -m venv environment`

Navigate to the environment: <br>
`cd environment`

Activate the environment: <br>
`source bin/activate`

Clone this repository (NOTE: You need to generate a GitHub SSH Key first! If you cannot do this, download this repo via HTTPS): <br>
`git clone <ssh-link>`

Navigate to the cloned git repo: <br>
`cd restaurants`

Install Python3 dependencies: <br>
`pip3 install -r requirements.txt`

Ensure MongoDB is running: <br>
`sudo systemctl stop mongodb` <br>
`sudo systemctl start mongodb`

Import db.json into MongoDB: <br>
`cd data` <br>
`mongoimport --host localhost --port 27017 --db viaplay --collection restaurants --type json --file ./db.json --jsonArray` <br>
`cd ..`

Start the server: <br>
`cd src` <br>
`python3 restaurants.py`

If you wish, you can host your API server using Ngrok. It's light-weight and simple. <br>
Download Ngrok and follow the instructions on their website (see website hyper-link above). <br>
Run `./ngrok http 5001` to launch ngrok. <br>
You can now visit the ngrok site generated for you (<hash>.io/restaurants) and visit all the API end-points there instead of at localhost. <br>
For the sake of this guide, we'll assume you're running this API on localhost.

You can now visit: <br>
`http://localhost:5001/restaurants` <br>
where you will see a list of all restaurants. <br>
Visit: `http://localhost:5001/restaurants/<id>` to see more detailed information on a specific restaurant. <br>

If you'd like to add a new restaurant, input the relevant information in test.json (while following the same format for all data inputs!), open a new terminal and run the following command: <br>
`curl -i -H "Content-Type: application/json" -X POST -d @test.json http://localhost:5001/add_restaurant`

If you'd like to delete an existing restaurant, open a new terminal and run the following command: <br>
`curl -X POST localhost:5001/delete_restaurant/<id>`

If you'd like to delete multiple existing restaurants at once, create a .json file and write down all the restaurant ID's in a list []. See del_test for example format. Then, run the following command in a new terminal: <br>
`curl -i -H "Content-Type: application/json" -X POST -d @restaurant_ids.json http://localhost:5001/delete_restaurants`

## Tasks
Implemented features:
* Task 1: An endpoint that lets the client get a list of all restaurants 
* Task 2: An endpoint that lets the client get more info on a single restaurant
* Task 3: An endpoint that accepts a POST request to add new restaurants to the DB
* Task 4: Functionality to delete restaurants from the DB through the API

## Possible improvements

* Could be good to do some form of regex-check to validate data input from .json file for the add_restaurant POST method.
* Prevent exact same data from being stored in the DB multiple times (to prevent DoS attacks or other malicious use)
* If we insert 50 new restaurants to a blank database, then delete restaurants 0-48, then newly inserted restaurants will have ID 50 and on, and not start back from 0. This can be fixed.
* Handle maximum allowable length of .json files during POSTs, to prevent DoS attacks/malicious use?
* No error handling is done on add_new_restaurants .json input file, so that'd probably be good to do.