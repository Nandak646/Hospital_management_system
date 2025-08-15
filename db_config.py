import mysql.connector
import os

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password_here',
    'database': 'nandu_db',
    'charset': 'utf8'
}

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "your_admin_password_here")

def connect_db():
    return mysql.connector.connect(**DB_CONFIG)
