PYTHON AND MONGODB

For raw project instructions see: https://umuzi-org.github.io/tech-department/projects/python-specific/mongo/

create environmental variables in your terminal/virtual environment:

~$ MONGO_DB='localhost'
~$ echo $MONGO_DB
~$ export MONGO_DB='localhost'



INTRODUCTION

Create a docker composition which will run mongodb. 

Instructions:
    - You are required to create a back-end service that will help capture basic information about prospective students who come to inquire at Umuzi.


REQUIREMENTS

Prerequisites: MongoDB and Python

This project requires the following modules:

pymongo==3.10.1
pytest==4.6.9


INSTALLATION

Install the following modules from your terminal or visit their respective websites, for further assistance and information.

    ~$ pip install pymongo

or visit: https://pypi.org/project/pymongo/

    ~$ pip install pytest

or visit: https://docs.pytest.org/en/stable/getting-started.html

NB! Make sure to Install these modules in your virtual environment. Check versions of modules to ensure they have been installed.



CONFIGURATION

After installations are completed, and have created a directory, do the following:

Make sure to work inside your virtual environment at all times. This is so that, your modules are recognised and will not be lost when working on a new terminal.

1. Create a docker-compose.yaml file, and fire it up using the following commands on your terminal:

    ~$ sudo systemctl start mongod
    ~$ docker-compose up

2. Start a new terminal, and open up a mongodb shell.To do this, run the following commands:

    ~$ docker container ls
NB!. Copy the container ID of your mongo database/container, and paste it in the next command.

    ~$ docker exec -it [container ID] mongo -u root

3. Setup database.
    - Create a database
    - Create a collection in the database you craeted.
    - Add required fields to your collection.

3. Write a Python script that will execute the following functions:

    - create_visitor (This should save the Visitor into the database)
    - list_visitors (This should return an array of all the visitor names and ids)
    - delete_visitor
    - update_visitor
    - visitor_details (Given a visitor’s id, return all information about that visitor)
    - delete_all

You are good to go.

