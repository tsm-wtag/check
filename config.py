import psycopg2

conn = psycopg2.connect( # need to change all the things for security
    dbname = "fastapi",
    user = "postgres",
    password = "123",
    host = "localhost",
    port = "5432"
)

#if(connection):
#    print("Database up!")
#else: 
#    print("Error message 404!!")
#cursor = connection.cursor()

