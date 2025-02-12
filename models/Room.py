from tabulate import tabulate

class Room:
    def __init__(self, room_id, room_type, price, availability=True):
        self.room_id = room_id
        self.room_type = room_type
        self.price = price
        self.availability = availability

    @staticmethod
    def add_room(conn, room_type, price):
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO rooms (room_type, price, availability) VALUES (%s, %s, True)",
                    (room_type, price)
                )
                conn.commit()
                print("Room added successfully")
        except Exception as e:
            print("Error adding room", e)

    @staticmethod
    def view_rooms(conn):
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM rooms")
                rooms = cur.fetchall()
                print(tabulate(rooms, headers=['Room ID', 'Type', 'Price', 'Available']))
        except Exception as e:
            print("Error viewing rooms", e)