class Booking:
    def __init__(self, booking_id, guest_id, room_id, check_in, check_out):
        self.booking_id = booking_id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in = check_in
        self.check_out = check_out

    @staticmethod
    def create_booking(conn, guest_id, room_id, check_in, check_out):
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT availability FROM rooms WHERE room_id = %s",(room_id,))
                available = cur.fetchone()[0]

                if available:

                    cur.execute (
                        "SELECT * FROM bookings WHERE room_id = %s AND check_in = %s ", (room_id, check_in)
                    )
                    existing_booking = cur.fetchone()

                    if existing_booking:
                        print("Error: room already booked")
                    else:
                        # new booking
                        cur.execute("INSERT INTO bookings (guest_id, room_id, check_in, check_out) VALUES (%s, %s, %s, %s)",(guest_id, room_id, check_in, check_out))
                        #borrowed
                        cur.execute(
                            "UPDATE rooms SET availability = FALSE WHERE room_id = %s",
                            (room_id,)
                        )
                        conn.commit()
                        print("Booking created successfully")
                else:
                    print("Room is not available")

        except Exception as e:
            print("Error creating booking: ", e)

