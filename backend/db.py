import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="mood_db",
        user="postgres",
        password="5742",
        port=5432
    )