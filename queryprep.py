# !/Users/mackmerriman/cos333/A3-cos333/queryprep.py

# Author: Mack Merriman
#-----------------------------------------------------------------------

def query_prep(filters):

    parameters = []

    for i in range(0, len(filters), 1):
        if filters[i]:
            filters[i] = (str(filters[i])
                          .upper()
                          .replace("%", "\\%")
                          .replace("_", "\\_"))

    # begin the perpared statement with the desired values,
    # the tables we need to query from, and the conditions
    # that must be met for the query to be accurate.
    stmt_str = "SELECT classid, dept, coursenum, area, title "
    stmt_str += "FROM classes, courses, crosslistings "
    stmt_str += "WHERE classes.courseid = courses.courseid "
    stmt_str += "AND courses.courseid = crosslistings.courseid "

    # if any of the flag values were provided by the users,
    # add them as a condition to the prepared statement.
    if filters[0]:
        stmt_str += "AND dept LIKE ? "
        parameters.append("%" + filters[0] + "%")

    if filters[1]:
        stmt_str += "AND coursenum LIKE ? "
        parameters.append("%" + filters[1] + "%")

    if filters[2]:
        stmt_str += "AND area LIKE ? "
        parameters.append("%" + filters[2] + "%")

    if filters[3]:
        stmt_str += "AND title LIKE ? "
        parameters.append("%" + filters[3] + "%")

    # if any flag conditions were added, add the escape char
    # and ensure results are ordered properly.
    if filters[0] or filters[1] or filters[2] or filters[3]:
        stmt_str += "ESCAPE '\\' "
    stmt_str += "ORDER BY dept ASC, coursenum ASC, classid ASC"

    return [stmt_str, parameters]
