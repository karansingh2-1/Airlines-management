from database import Database

class Booking:
    def __init__(self):
        self.db = Database()

    def create_booking(self, flight_id, passenger_id):
        query = """
        INSERT INTO bookings (flight_id, passenger_id)
        VALUES (%s, %s)
        """
        self.db.execute_query(query, (flight_id, passenger_id))
        print("Booking created successfully.")

    def view_bookings(self, passenger_id):
        query = """
        SELECT b.booking_id, f.flight_number, f.destination, f.departure, b.booking_date, b.status
        FROM bookings b
        JOIN flights f ON b.flight_id = f.flight_id
        WHERE b.passenger_id = %s
        """
        bookings = self.db.fetch_all(query, (passenger_id,))
        return bookings
