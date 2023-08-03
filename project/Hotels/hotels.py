from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user
from hotel.forms import CustomerLoginForm
from hotel.models import load_user

import psycopg2



Hotels = Blueprint('Hotels', __name__)



def get_hotels_data():
    conn = psycopg2.connect(
        database="INSERT_DB_NAME",
        user="postgres",
        password="INSERT_PASSWORD",
        host="127.0.0.1",
        port="5432",
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hotels;")
    hotels_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return hotels_data


@Hotels.route('/')
def home():
    return render_template('home.html')

@Hotels.route('/login')
def login():
    return render_template('login.html')  # Assuming you have a 'home.html' template for the home page

@Hotels.route('/hotels')
def hotels():
    return render_template('hotels.html', hotels_data=get_hotels_data())

@Hotels.route('/sort_hotels_by_column/<string:column_name>')
def sort_hotels_by_column(column_name):
    valid_columns = ['ID', 'Owner', 'Name', 'Type', 'Location', 'URL', 'Availability']
    if column_name not in valid_columns:
        return "Invalid column name", 400

    conn = psycopg2.connect(
        database="INSERT_DB_NAME",
        user="postgres",
        password="INSERT_PASSWORD",
        host="127.0.0.1",
        port="5432",
    )

    cursor = conn.cursor()

    query = f"SELECT * FROM hotels ORDER BY {column_name};"
    cursor.execute(query)
    sorted_hotels_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('hotels.html', hotels_data=sorted_hotels_data)

@Hotels.route('/reserve_hotel', methods=['POST'])
def reserve_hotel():
    if request.method == 'POST':
        hotel_id = int(request.form.get('hotel_id'))
        conn = psycopg2.connect(
            database="INSERT_DB_NAME",
            user="postgres",
            password="INSERT_PASSWORD",
            host="127.0.0.1",
            port="5432",
        )

        cursor = conn.cursor()
        
        if not current_user.is_authenticated:
            flash('Please login in order to make a reservation.')
            return redirect('login') 
    else:
        flash('Please login in order to see your reservations.')
        return redirect('login')
    try:
        # First, check if the hotel is still available
        cursor.execute("SELECT Availability FROM hotels WHERE ID = %s;", (hotel_id,))
        hotel_availability = cursor.fetchone()

        if hotel_availability[0] == "Available":

            sql = """UPDATE hotels SET Availability = 'Reserved' WHERE ID = %s;
            """
            cursor.execute(sql, (hotel_id,))
            sql = """INSERT INTO reservations (Username, HotelID) VALUES ('test-customer', %s);
            """
            cursor.execute(sql, (hotel_id,))

            conn.commit()
            flash('Reservation successful!', 'success')
        else:
            flash('Hotel is already reserved by someone else.', 'warning')

    except Exception as e:
        conn.rollback()
        flash('Error occurred while processing the reservation.', 'danger')

    cursor.close()
    conn.close()

    return redirect('hotels')
@Hotels.route('/cancel_reservation', methods=['POST'])
def cancel_reservation():
    if request.method == 'POST':
        hotel_id = int(request.form.get('hotel_id'))

        conn = psycopg2.connect(
            database="INSERT_DB_NAME",
            user="postgres",
            password="INSERT_PASSWORD",
            host="127.0.0.1",
            port="5432",
        )

        cursor = conn.cursor()
        if not current_user.is_authenticated:
            flash('Please login in order to cancel reservations.')
            return redirect('login')
        try:
            # First, check if the hotel is currently reserved
            cursor.execute("SELECT Availability FROM hotels WHERE ID = %s;", (hotel_id,))
            hotel_availability = cursor.fetchone()

            if hotel_availability[0] == "Reserved":
                # If the hotel is reserved, update the availability to "Available"
                cursor.execute("UPDATE hotels SET Availability = 'Available' WHERE ID = %s;", (hotel_id,))
                cursor.execute("DELETE FROM reservations WHERE hotelid = %s;", (hotel_id,))
                # Add any additional logic here for handling reservation cancellation (e.g., removing from reservations table)

                conn.commit()
                flash('Reservation cancelled successfully!', 'success')
            else:
                flash('Hotel is not reserved at the moment.', 'warning')

        except Exception as e:
            conn.rollback()
            flash('Error occurred while cancelling the reservation.', 'danger')

        cursor.close()
        conn.close()

        return redirect('hotels')