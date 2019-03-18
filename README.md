# Kanban-Board
Flask Project for CS162

## Setting Up Virtual Environment
### Create a Virtual Environment

```bash
$ python3 -m virtualenv venv
```
To activate the virtual environment, run:

```bash
$ source venv/bin/activate
```

## Installing Dependencies
To successfully run the application, dependencies are required, please run:

```bash
$ pip3 install -r requirements.txt 
```

## Setting up a database:
We use a sqlite database in this project, to set up the database, go to the terminal and enter:

```bash
$ python3
```

Once your on the python console, enter the following commands:

```bash
$ from kanban import db
$ db.session.drop_all()
$ db.session.create_all()
```

## Running the application
Once you installed everything necessary, go to the root directory of the project and run:

```bash
$ python3 app.py
```

## Testing 
To run the unit tests, be sure to run the following command and the project directory:

```bash
$ cd kanban
$ python3 -m unittest discover tests
```

## Project Structure

```bash
Directory/Kanban-Board
├── kanban/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── models.py
│   ├── templates/
│   │   ├── add.html
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── items.html
│   │   ├── login.html
│   │   └── register.html
│   ├── static/
│   │   └── main.css
│   └── tests
│       ├── test_basic.py
│       └── test_function.py
├── requirements.txt
├── run.py
└── venv/
```

## Description of Application
In the Simple Kanban Board, users are able to register for an account, log in, and enjoy the functionalities of a kanban board. Users can add a new todo item (including a deadline), which would by default be under the "Todo" table, and are able to move it to the other tables. When the item is completed (listed under "Done"), the user has the option to delete the item. At any point the user is also able to click on the items to inspect the descriptions of each todo item. Each user will only see the todo items created by themselves, as this is a very personalized application.
