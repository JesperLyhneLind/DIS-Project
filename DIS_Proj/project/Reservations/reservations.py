from flask import render_template, url_for, flash, redirect, request, Blueprint
from hotel import app, conn, bcrypt
from hotel.forms import CustomerLoginForm
from hotel.models import Customer
from flask_login import login_user, current_user, logout_user, login_required
import psycopg2

Reservations = Blueprint('Reservations', __name__)

def get_hotels_data():
    conn = psycopg2.connect(
        database="INSERT_DB_NAME",
        user="postgres",
        password="INSERT_PASSWORD",
        host="127.0.0.1",
        port="5432",
    )

    cursor = conn.cursor()
    cursor.execute("SELECT username, id, owner, name, type, location, url, availability FROM reservations INNER JOIN hotels on reservations.hotelid = hotels.id;")
                   
                   
    #SELECT * FROM hotels WHERE Availability = 'Reserved';")
    

    hotels_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return hotels_data


@Reservations.route('/')
def home():
    return render_template('home.html')




@Reservations.route('/reservations')
def reservations():
    if current_user.is_authenticated:
        return render_template('reservations.html', hotels_data=get_hotels_data())
    else:
        flash('Please login in order to see your reservations.')
        return redirect('login')


@Reservations.route('/cancel_reservations', methods=['POST'])
def cancel_reservations():
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

        try:
            # First, check if the hotel is currently reserved
            cursor.execute("SELECT username, id, owner, name, type, location, url, availability FROM reservations INNER JOIN hotels on reservations.hotelid = hotels.id;")
            hotel_availability = cursor.fetchone()

            if hotel_availability[7] == "Reserved":
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

        return redirect('reservations')