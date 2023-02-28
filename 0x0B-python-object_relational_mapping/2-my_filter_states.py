#!/usr/bin/python3
"""connect to MySQLdb"""
import MySQLdb
import sys


def selectNstate():
    """SQL Selection Function"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'".format(sys.argv[4]))
    y = cur.fetchall()
    for x in y:
        print(x)

    cur.close()
    db.close()


if __name__ == "__main__":
    selectNstate()
