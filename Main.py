from DBConnection import connect_db
from Room import Room
from Guest import Guest
from Booking import Booking

def main():
    conn = connect_db()
    while True:
        print("\n Hotel Booking System")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Add Guest")
        print("4. View Guests")
        print("5. Create Booking")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_type = input("Enter room type: ")
            price = float(input("Enter room price per night: "))
            Room.add_room(conn, room_type, price)
        elif choice == "2":
            Room.view_rooms(conn)
        elif choice == "3":
            name = input("Enter guest name: ")
            contact = input("Enter guest contact information: ")
            Guest.add_guests(conn, name, contact)
        elif choice == "4":
            Guest.view_guests(conn)
        elif choice == "5":
            guest_id = int(input("Enter guest ID: "))
            room_id = int(input("Enter room ID: "))
            check_in = input("Enter check in date (YYYY-MM-DD): ")
            check_out = input("Enter check out date (YYYY-MM-DD): ")
            Booking.create_booking(conn, guest_id, room_id, check_in, check_out)
        elif choice == "0":
            conn.close()
            print("Exiting the system. Bye Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
