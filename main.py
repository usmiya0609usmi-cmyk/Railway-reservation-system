import random

# Total seats
TOTAL_SEATS = 50
available_seats = list(range(1, TOTAL_SEATS + 1))

# Store bookings
bookings = {}

# Generate booking ID
def generate_id():
    return random.randint(1000, 9999)

# Check availability
def check_availability():
    print(f"\nAvailable Seats: {len(available_seats)}")
    print(available_seats)

# Book ticket
def book_ticket():
    if not available_seats:
        print("\nNo seats available!")
        return

    name = input("Enter name: ")
    age = input("Enter age: ")

    seat = available_seats.pop(0)
    booking_id = generate_id()

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat
    }

    print(f"\nTicket booked successfully!")
    print(f"Booking ID: {booking_id}, Seat No: {seat}")

# View ticket
def view_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        data = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Seat No: {data['seat']}")
    else:
        print("Booking not found!")

# Cancel ticket
def cancel_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        seat = bookings[booking_id]['seat']
        available_seats.append(seat)
        del bookings[booking_id]

        print("Ticket cancelled successfully!")
    else:
        print("Invalid Booking ID!")

# Menu
def menu():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            check_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

# Run program
menu()
