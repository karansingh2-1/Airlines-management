import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="karansingh21",
            database="airline_db"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    def close(self):
        self.connection.close()

import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        # Create a connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",        # Replace with your MySQL server address
            user="root",             # Replace with your MySQL username
            password="karansingh21",# Replace with your MySQL password
            database="airline_db"    # Replace with your database name
        )

        if connection.is_connected():
            print("Connection to MySQL was successful!")
            return connection

    except Error as e:
        print(f"Error: {e}")
        return None

