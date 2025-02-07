import psycopg2

def connect_db():
    return psycopg2.connect(dbname = "hoteldb",
                            user = "postgres",
                            password = "135790",
                            host = "127.0.0.1",)

