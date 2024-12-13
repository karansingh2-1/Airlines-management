from database import Database
from views.admin_view import admin_menu
from views.user_view import user_menu

def main():
    print("Welcome to Airline Booking System!")
    print("1. Admin Login")
    print("2. User Access")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        admin_menu()
    elif choice == "2":
        user_menu()
    elif choice == "3":
        print("Exiting the system. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
