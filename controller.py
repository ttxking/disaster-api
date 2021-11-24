import sys
from flask import abort
import pymysql as mysql
from config import OPENAPI_AUTOGEN_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_AUTOGEN_DIR)
from openapi_server import models

def db_cursor():
    return mysql.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWD,
                         db=DB_NAME).cursor()

def get_earthquake():
    with db_cursor() as cs:
        cs.execute("""
            SELECT center, magnitude
            FROM earthquake
        """)
        result = [models.EarthquakeBasic(*row) for row in cs.fetchall()]
        return result

def get_earthquake_details(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT  center, magnitude, date, lat, lon, depth, phrase
            FROM earthquake
            WHERE center like %s
        """, [pro])
        result = [models.EarthquakeDetail(*row) for row in cs.fetchall()]
        return result

def get_average_magnitude_and_phrase(province):
    pro = '%' + province + '%'
    with db_cursor() as cs:
        cs.execute("""
            SELECT ROUND(AVG(magnitude),2) average_magnitude, ROUND(AVG(phrase),2) average_phrase
            FROM(
            SELECT  center, magnitude, date, lat, lon, depth, phrase
            FROM earthquake
            WHERE center like %s) eq
        """, [pro])
        result = cs.fetchone()
        if result:
            return models.EarthquakeAverage(*result)
        else:
            abort(404)

def get_landslide():
    with db_cursor() as cs:
        cs.execute("""
            SELECT province, `risk-landslide-area`
            FROM landslide
        """)
        result = [models.LandslideBasic(*row) for row in cs.fetchall()]
        return result

