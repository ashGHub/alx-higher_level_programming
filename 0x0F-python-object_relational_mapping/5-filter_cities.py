#!/usr/bin/python3
"""Filters city by state from database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
                   FROM cities \
                   INNER JOIN states \
                   ON cities.state_id = states.id \
                   WHERE states.name LIKE BINARY %s \
                   ORDER BY cities.id ASC",
                   (sys.argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row[0], end="")
        if row != query_rows[-1]:
            print(", ", end="")
    print()
    cursor.close()
    db.close()
