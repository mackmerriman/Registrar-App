def query_display(table):

    # print out the top of the table in the desired fashion.

    # print out the desired values in the order according
    # to the columns above. Left padding length is arbitrarily
    # chosen by the number of dashes below each the column title.

    ftable = []

    for row in table:
        line = ""

        clsid = str(row[0]).rjust(5, " ")
        line += f"{clsid} "

        dept = str(row[1]).rjust(4, " ")
        line += f"{dept} "

        crsnum = str(row[2]).rjust(6, " ")
        line += f"{crsnum} "

        area = str(row[3]).rjust(4, " ")
        line += f"{area} "

        title = str(row[4])
        line += f"{title}"

        ftable.append(line)

    return ftable
