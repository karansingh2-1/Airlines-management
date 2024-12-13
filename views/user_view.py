from models.flight import Flight
from models.passenger import Passenger
from models.booking import Booking

def user_menu():
    flight = Flight()
    passenger = Passenger()
    booking = Booking()

    print("User Menu")
    email = input("Enter your email to continue: ")
    user = passenger.get_passenger(email)

    if not user:
        print("User not found. Please register.")
        full_name = input("Enter Full Name: ")
        phone_number = input("Enter Phone Number: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        passenger.register_passenger(full_name, email, phone_number, dob)

    while True:
        print("\n1. Search Flights")
        print("2. Book a Flight")
        print("3. View Bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            destination = input("Enter Destination: ")
            departure = input("Enter Departure City: ")
            flights = flight.search_flights(destination, departure)
            if flights:
                for f in flights:
                    print(f"Flight ID: {f[0]}, Flight Number: {f[1]}, Seats Available: {f[6]}, Price: ${f[7]}")
            else:
                print("No flights found.")
        elif choice == "2":
            flight_id = int(input("Enter Flight ID: "))
            passenger_id = user[0]
            booking.create_booking(flight_id, passenger_id)
        elif choice == "3":
            passenger_id = user[0]
            bookings = booking.view_bookings(passenger_id)
            for b in bookings:
                print(b)
        elif choice == "4":
            print("Exiting user menu.")
            break
        else:
            print("Invalid choice.")
