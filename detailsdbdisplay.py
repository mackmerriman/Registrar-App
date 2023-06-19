import sys
import sqlite3
import contextlib

# initialize the titles for two groups of columns that are
# "grouped" together.
classesfields = ["Days:", "Start time:", "End time:",
                 "Building:", "Room:"]
coursesfields = ["Area:", "Title:", "Description:", "Prerequisites:"]

# connect to the database, throw an error if unsuccessful.
def details_db_display(classid):

    try:
        with sqlite3.connect("reg.sqlite",
                             isolation_level=None) as connection:

            with contextlib.closing(connection.cursor()) as cursor:

                tables = []
                fail = 0

                cursor.execute("SELECT classid FROM classes "
                               "WHERE classid = ?",
                               (classid,))
                table = cursor.fetchall()

                if not table:
                    fail = 2

                tables.append(table)

                cursor.execute("SELECT courseid, days, "
                               "starttime, endtime, bldg, roomnum "
                               "FROM classes "
                               "WHERE classid = ?", (classid,))
                table = cursor.fetchall()
                tables.append(table)

                cursor.execute("SELECT courseid FROM classes "
                               "WHERE classid = ?",
                               (classid,))
                table = cursor.fetchall()
                tables.append(table)

                cursor.execute("SELECT dept, coursenum FROM classes, \
                               crosslistings WHERE classid = ? "
                               "AND classes.courseid = "
                               "crosslistings.courseid "
                               "ORDER BY dept ASC, coursenum ASC",
                               (classid,))
                table = cursor.fetchall()
                tables.append(table)

                cursor.execute("SELECT area, title, descrip, prereqs "
                               "FROM classes, courses "
                               "WHERE classid = ? "
                               "AND classes.courseid = "
                               "courses.courseid", (classid,))
                table = cursor.fetchall()
                tables.append(table)

                cursor.execute("SELECT profname "
                               "FROM classes, coursesprofs, profs "
                               "WHERE classid = ? AND classes.courseid "
                               "= coursesprofs.courseid "
                               "AND coursesprofs.profid = profs.profid "
                               "ORDER BY profname ASC", (classid,))
                table = cursor.fetchall()
                tables.append(table)

    except Exception as ex:
        print(ex, file=sys.stderr)
        return None, 1

    return tables, fail
