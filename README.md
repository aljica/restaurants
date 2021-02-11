# Restaurants

This repository contains an implementation of a REST API that can read and write into the provided db while providing endpoints to clients from which they will be able to perform basic CRUD (Create, Read, Update, Delete) operations on the database. 

## Prerequisites

* Python3
* [MongoDB](https://www.mongodb.com/)
* [Ngrok](https://ngrok.com/)

**Libraries**

* Python Standard Library >= 3.8.5
* [Flask](https://pypi.org/project/Flask/)
* [pymongo](https://pypi.org/project/pymongo/)

## Installation

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

## Tasks
Some of the suggested features you could try are listed here (Please attempt at least three features here)
* An endpoint that lets the client get a list of all restaurants 
* An endpoint that lets the client get more info on a single restaurant
* An endpoint that accepts a POST request to add new restaurants to the DB
* Functionality to delete restaurants from the DB through the API
* Functionality to fetch a sorted list of restaurants based on relevant attributes
* Functionality to fetch a filtered list of restaurants based on relevant attributes

## Possible improvements

* Could be good to do some form of regex-check to validate data input from .json file for the add_restaurant POST method.
* Prevent exact same data from being stored in the DB multiple times (to prevent DDoS attacks or other malicious use)
