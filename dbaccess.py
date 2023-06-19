import sys
import sqlite3
import contextlib

def db_access(statement):
    try:
        with sqlite3.connect("reg.sqlite",
                             isolation_level=None) as connection:

            with contextlib.closing(connection.cursor()) as cursor:

                cursor.execute(statement[0], statement[1])

                table = cursor.fetchall()

                return table, False

    except Exception as ex:
        print(ex, file=sys.stderr)
        return None, True
