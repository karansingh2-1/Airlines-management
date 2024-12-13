from database import Database

class Flight:
    def __init__(self):
        self.db = Database()

    def add_flight(self, flight_id, destination, departure_time, seats):
        query = "INSERT INTO flights (flight_id, destination, departure_time, seats) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (flight_id, destination, departure_time, seats))

    def list_flights(self):
        query = "SELECT * FROM flights"
        return self.db.fetch_all(query)

    def delete_flight(self, flight_id):
        query = "DELETE FROM flights WHERE flight_id = %s"
        self.db.execute_query(query, (flight_id,))
