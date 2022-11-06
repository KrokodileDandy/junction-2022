"""Database interface."""

import psycopg2
from config import config

def run_query(query, record=None):
    """ Connect to the PostgreSQL database server """
    try:
        print('Initialize database connection...')
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        print('Prepare query...')
        cursor.execute(query)
        print('Fetch results...')
        result = cursor.fetchall()

        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection error!")
        raise Exception(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
