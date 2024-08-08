from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app: Flask):
    mysql.init_app(app)
