#!/usr/bin/python3
""" no injections this time! """
import sys
import MySQLdb

if __name__ == "__main__":
    with MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host='localhost',
            port=3306,
    )as conn:
        cur = conn.cursor()
        query = """ SELECT c.name
                    FROM states as s, cities as c
                    WHERE s.name = '{:s}'
                    ORDER BY c.id ASC
                """
        cur.execute(query.format(sys.argv[4]))
        cities = cur.fetchall()
        for city in cities:
            print(city)
        cur.close()
