#!/usr/bin/python3
"""
Filter a state on states list from the database hbtn_0e_0_usa
This time, the script is safe from MySQL injections!
"""


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
    cursor.execute("SELECT * \
                   FROM states \
                   WHERE name LIKE BINARY %s \
                   ORDER BY id ASC",
                   (sys.argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
