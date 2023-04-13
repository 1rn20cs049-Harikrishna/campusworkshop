"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpuj82qv2dcb91du70-a.oregon-postgres.render.com",
        database="todo_53yc",
        user="hari",
        password="6Rcm22iqnGHc94wEbaCG4YhHLf3sP0HJ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
