#!/usr/bin/python3
"""Filter a state on states list from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db_conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    cursor = db_conn.cursor()
    # BINARY : make it case sensitive
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db_conn.close()
