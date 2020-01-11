pconnector code
import psycopg2
from psycopg2 import Error

    connection = psycopg2.connect(user = "surajkumarjha",
                                  password = "postgress",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO chirag(")