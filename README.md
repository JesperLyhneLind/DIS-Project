# DIS-Project
DIS-Project - Hotel reservation

SETTING UP THE DATABASE:

Open pgAdmin or your preferred database management tool.

Create a new database, or use an existing one, jus make sure to modify the database name and password in our files:
__init__.p, hotels.py and reservations.py.
There are several places in the hotels and reservations file to modify (ctrl + f) recommended.

Run the following scripts in the provided order to set up the database:

schema.sql: Drops and Creates the necessary schema for the database.
schema_insert.sql: Inserts dummy data into the tables for testing purposes.


HOW TO RUN THE WEB APPLICATION:

Make sure you have all the necessary packages installed. You can install them using the following command in your terminal:

'pip install -r requirements.txt'

Go the the hotels directory and type the following command to run the web application:

'python3 run.py', or perhaps just 'python run.py'

Open a web browser and go to http://127.0.0.1:5000 to access the application.

Click on "Login" in the navigation bar and log in using one of the provided dummy accounts:
Some functionality is locked wihout being logged in:

Username: 'test-customer'
Password: 'hotels'

After logging in, you will be redirected to the home page. You can use the navigation bar to reach 'About' and read about the functionalities of the website.
