# write all your SQL queries in this file.
from datetime import datetime
from project import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


class Customer(tuple, UserMixin):
    def __init__(self, user_data):
        self.username = user_data[0]
        self.password = user_data[1]

    def get_id(self):
       return (self.username)

@login_manager.user_loader
def load_user(username):
    cur = conn.cursor()
    sql = """
    SELECT * FROM customer
    WHERE username = 'test-customer'
    """
    cur.execute(sql, (username,))#måske fjern (username,)
    user = Customer(cur.fetchone()) if cur.rowcount > 0 else None
    cur.close()
    return user
