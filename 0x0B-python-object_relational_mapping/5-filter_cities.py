#!/usr/bin/python3
"""connect to MySQLdb"""
import MySQLdb
import sys


def selectNstate():
    """SQL Selection Function"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities INNER JOIN states ON cities.state_id = \
                states.id ORDER BY cities.id")

    city_list = [city[2] for city in cur.fetchall() if city[4] == sys.argv[4]]
    print(", ".join(city_list))

    cur.close()
    db.close()


if __name__ == "__main__":
    selectNstate()
