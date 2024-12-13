from database import Database

class Passenger:
    def __init__(self):
        self.db = Database()

    def register_passenger(self, full_name, email, phone_number, date_of_birth):
        query = """
        INSERT INTO passengers (full_name, email, phone_number, date_of_birth)
        VALUES (%s, %s, %s, %s)
        """
        self.db.execute_query(query, (full_name, email, phone_number, date_of_birth))
        print("Passenger registered successfully.")

    def get_passenger(self, email):
        query = "SELECT * FROM passengers WHERE email = %s"
        passenger = self.db.fetch_one(query, (email,))
        return passenger
