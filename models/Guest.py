from tabulate import tabulate

class Guest:
    def __init__(self, guest_id, name, contact):
        self.guest_id = guest_id
        self.name = name
        self.contact = contact

    @staticmethod
    def add_guests(conn, name, contact):
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO guests (name, contact) VALUES (%s, %s)",
                            (name, contact))
                conn.commit()
                print("Guest added successfully")
        except Exception as e:
            print("Error adding guest:", e)

    @staticmethod
    def view_guests(conn):
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM guests")
                guests = cur.fetchall()
                print(tabulate(guests, headers=["Guest ID", "Name", "Contact"]))
        except Exception as e:
            print("Error viewing guests:", e)
