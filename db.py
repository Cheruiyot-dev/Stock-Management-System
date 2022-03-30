import os
import psycopg2

# connecting to an existing database
conn = psycopg2.connect(
        user="postgres",
        password="1092",
        host= "localhost",
        port="5432",
        database="myduka")

# Open a cursor to perform database operations
cur = conn.cursor()
