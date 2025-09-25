import psycopg2
import os
from contextlib import contextmanager
from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import DictCursor

DATABASE_URL = os.environ['DATABASE_URL']
pool = ThreadedConnectionPool(1, 100, dsn=DATABASE_URL, sslmode='require')

@contextmanager
def get_db_connection():
    try:
        connection = pool.getconn()
        yield connection
    finally:
        pool.putconn(connection)

@contextmanager
def get_db_cursor(commit=False):
    with get_db_connection() as connection:
      cursor = connection.cursor(cursor_factory=DictCursor)
      # cursor = connection.cursor()
      try:
          yield cursor
          if commit:
              connection.commit()
      finally:
          cursor.close()


def save_guest(guest_name):
    with get_db_cursor(True) as cur:
        cur.execute("""
            INSERT INTO guests (name)
            VALUES (%s)
        """,
        (guest_name,))

def get_guests():
    guests = []
    with get_db_cursor(False) as cur:
        cur.execute("""
            SELECT *
            FROM guests
        """)

        for row in cur:
            guests.append(row["name"])
    return guests