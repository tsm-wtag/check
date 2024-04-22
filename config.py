import psycopg2
import os

conn = psycopg2.connect( # need to change all the things for security
    dbname = os.environ.get('DB_NAME'),
    user = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD'),
    host = os.environ.get('DB_HOST'),
    port = os.environ.get('DB_PORT'),
)

#if(connection):
#    print("Database up!")
#else: 
#    print("Error message 404!!")
#cursor = connection.cursor()

