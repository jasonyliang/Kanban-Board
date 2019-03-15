# Kanban-Board
Flask Project for CS162

## Setting Up Virtual Environment
### Create a Virtual Environment
$ python3 -m virtualenv venv
To activate the virtual environment, run:
$ source venv/bin/activate

## Installing Dependencies
To successfully run the application, dependencies are required, please run:
$ pip3 install -r requirements.txt 

## Setting up a database:
We use a sqlite database in this project, to set up the database, go to the terminal and enter:
$ python3
Once your on the python console, enter the following commands:
$ from kanban import db
$ db.session.drop_all()
$ db.session.create_all()

## Running the application
Once you installed everything necessary, go to the root directory of the project and run:
$ python3 app.py

