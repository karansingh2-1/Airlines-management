import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import mysql.connector

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="karansingh21",
            database="airline_db"
        )
        return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None

# Function to add a flight
def add_flight():
    flight_no = flight_number_entry.get()
    destination = destination_entry.get()
    departure = departure_entry.get()
    dep_time = departure_time_entry.get()
    arr_time = arrival_time_entry.get()
    seats = seats_entry.get()
    price = price_entry.get()

    if not (flight_no and destination and departure and dep_time and arr_time and seats and price):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    if not validate_time(dep_time) or not validate_time(arr_time):
        messagebox.showerror("Input Error", "Time must be in HH:MM format!")
        return

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
            INSERT INTO flights (flight_number, destination, departure, departure_time, arrival_time, seats_available, price)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (flight_no, destination, departure, dep_time, arr_time, seats, price))
            connection.commit()
            messagebox.showinfo("Success", "Flight added successfully!")
            clear_fields()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()

# Function to list flights
def list_flights():
    for row in flights_tree.get_children():
        flights_tree.delete(row)

    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM flights"
            cursor.execute(query)
            rows = cursor.fetchall()

            for row in rows:
                flights_tree.insert("", tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            connection.close()

# Function to validate time format
def validate_time(time_str):
    import re
    return bool(re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_str))

# Function to clear input fields
def clear_fields():
    flight_number_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)
    departure_time_entry.delete(0, tk.END)
    arrival_time_entry.delete(0, tk.END)
    seats_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Airline Booking Management System")
root.geometry("900x700")

# Notebook for Tabs
tabs = ttk.Notebook(root)
tabs.pack(expand=1, fill="both")

# Add Flight Tab
add_flight_tab = ttk.Frame(tabs)
tabs.add(add_flight_tab, text="Add Flight")

# Add Flight Input Fields
tk.Label(add_flight_tab, text="Flight Number:").grid(row=0, column=0, padx=10, pady=5)
flight_number_entry = tk.Entry(add_flight_tab)
flight_number_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Destination:").grid(row=1, column=0, padx=10, pady=5)
destination_entry = tk.Entry(add_flight_tab)
destination_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Departure:").grid(row=2, column=0, padx=10, pady=5)
departure_entry = tk.Entry(add_flight_tab)
departure_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Departure Time (HH:MM):").grid(row=3, column=0, padx=10, pady=5)
departure_time_entry = tk.Entry(add_flight_tab)
departure_time_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Arrival Time (HH:MM):").grid(row=4, column=0, padx=10, pady=5)
arrival_time_entry = tk.Entry(add_flight_tab)
arrival_time_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Seats Available:").grid(row=5, column=0, padx=10, pady=5)
seats_entry = tk.Entry(add_flight_tab)
seats_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(add_flight_tab, text="Price:").grid(row=6, column=0, padx=10, pady=5)
price_entry = tk.Entry(add_flight_tab)
price_entry.grid(row=6, column=1, padx=10, pady=5)

# Buttons for Add Flight Tab
tk.Button(add_flight_tab, text="Add Flight", command=add_flight).grid(row=7, column=0, columnspan=2, pady=10)

# List Flights Tab
list_flights_tab = ttk.Frame(tabs)
tabs.add(list_flights_tab, text="List Flights")

# Treeview for Flights
flights_tree = ttk.Treeview(list_flights_tab, columns=("Flight ID", "Flight Number", "Destination", "Departure", "Departure Time", "Arrival Time", "Seats", "Price"), show="headings")
flights_tree.heading("Flight ID", text="Flight ID")
flights_tree.heading("Flight Number", text="Flight Number")
flights_tree.heading("Destination", text="Destination")
flights_tree.heading("Departure", text="Departure")
flights_tree.heading("Departure Time", text="Departure Time")
flights_tree.heading("Arrival Time", text="Arrival Time")
flights_tree.heading("Seats", text="Seats")
flights_tree.heading("Price", text="Price")
flights_tree.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(list_flights_tab, text="Load Flights", command=list_flights).pack(pady=10)

# Run the Application
root.mainloop()
