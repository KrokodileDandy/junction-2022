#!/usr/bin/python
import psycopg2
from config import config

conn = None
def connect():
    conn = None
    """ Connect to the PostgreSQL database server """
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def run_query(query, record=None):
    try:
        if (record):
            conn.execute(query, record)
        else:
            conn.execute(query)
        conn.commit()
        return True
    except (Exception, psycopg2.Error) as error:
        print("Failed to run query.")
        return False

def show_table(table_name):
    query = "SELECT * FROM %s"
    run_query(query, table_name)