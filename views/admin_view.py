from models.flight import Flight

def admin_menu():
    flight = Flight()

    while True:
        print("\nAdmin Menu")
        print("1. Add Flight")
        print("2. List Flights")
        print("3. Delete Flight")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            flight_id = input("Enter Flight ID: ")
            destination = input("Enter Destination: ")
            departure_time = input("Enter Departure Time: ")
            seats = input("Enter Number of Seats: ")
            flight.add_flight(flight_id, destination, departure_time, seats)
            print("Flight added successfully.")
        elif choice == "2":
            flights = flight.list_flights()
            for f in flights:
                print(f)
        elif choice == "3":
            flight_id = input("Enter Flight ID to delete: ")
            flight.delete_flight(flight_id)
            print("Flight deleted successfully.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
