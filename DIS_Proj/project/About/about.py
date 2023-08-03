from flask import render_template, url_for, flash, redirect, request, Blueprint
from project import app, conn, bcrypt
from project.forms import CustomerLoginForm
from project.models import Customer
import psycopg2

About = Blueprint('About', __name__)

@About.route('/about')
def about():
    return render_template('about.html')  # Assuming you have a 'home.html' template for the home page

@About.route('/home')
def home():
    return render_template('home.html')  # Assuming you have a 'home.html' template for the home page

# @About.route('/login')
# def login():
#     return render_template('login.html')  # Assuming you have a 'home.html' template for the home page




# @About.route('/hotels')
# def hotels():
#     hotels_data = get_hotels_data()
#     return render_template('hotels.html')  # Assuming you have a 'hotels.html' template for the hotels page



