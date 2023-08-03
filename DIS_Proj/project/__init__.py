from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

# set your own database
db = "dbname='INSERT_DB_NAME' user='postgres' host='127.0.0.1' password = 'INSERT_PASSWORD'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from project.Login.login import Login
from project.Hotels.hotels import Hotels
from project.About.about import About
from project.Reservations.reservations import Reservations


app.register_blueprint(Login)
app.register_blueprint(Hotels)
app.register_blueprint(About)
app.register_blueprint(Reservations)
