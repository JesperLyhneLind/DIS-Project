from flask import render_template, url_for, flash, redirect, Blueprint
from project import bcrypt
from project.forms import CustomerLoginForm
from flask_login import login_user, logout_user, current_user
from project.models import load_user

Login = Blueprint('Login', __name__)



@Login.route("/about")
def about():
    return render_template('about.html', title='About')

@Login.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You already are logged in')
        return redirect('home')

    form = CustomerLoginForm()
    if form.validate_on_submit():
        user = load_user(form.id.data)
        if user != None and bcrypt.check_password_hash(user[1], form.password.data):
            login_user(user)
            flash('Login successful.','success')
            return redirect('home')
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template("login.html", form=form)


@Login.route("/logout")
def logout():
    logout_user()
    flash('You have been logged out.', 'succes')
    return redirect('home')
