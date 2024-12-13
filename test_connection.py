from database import connect_to_database

def test_connection():
    connection = connect_to_database()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        for table in cursor.fetchall():
            print(table)
        connection.close()

if __name__ == "__main__":
    test_connection()
