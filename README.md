# Restaurants

This repository contains an implementation of a REST API that can read and write into the provided db while providing endpoints to clients from which they will be able to perform basic CRUD (Create, Read, Update, Delete) operations on the database. 

## Prerequisites

* Python3
* MongoDB

**Libraries**

* Python Standard Library >= 3.8.5
* [Flask] (https://pypi.org/project/Flask/)
* [pymongo] (https://pypi.org/project/pymongo/)

## Installation

Install Python3, MongoDB and the required libraries.
Ubuntu/Debian: <br>
`sudo apt install python3`
`sudo apt install mongodb`
`sudo apt install python3-pip`
`pip3 install -r requirements.txt` (This will install flask and pymongo - it is advisable that you run this command inside the virtual environment, see below)

Clone this repository (NOTE: You need to generate a GitHub SSH Key first! If you cannot do this, download this repo using via HTTPS): <br>
`git clone <ssh-link>`

Setup Python3 virtual environment: <br>
`python3 -m venv environment`

Navigate to the environment: <br>
`cd environment`



## Tasks
Some of the suggested features you could try are listed here (Please attempt at least three features here)
* An endpoint that lets the client get a list of all restaurants 
* An endpoint that lets the client get more info on a single restaurant
* An endpoint that accepts a POST request to add new restaurants to the DB
* Functionality to delete restaurants from the DB through the API
* Functionality to fetch a sorted list of restaurants based on relevant attributes
* Functionality to fetch a filtered list of restaurants based on relevant attributes