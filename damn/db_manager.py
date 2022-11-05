import psycopg2
from config import config


def run_query(query, record=None):
    """ Connect to the PostgreSQL database server """
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        cursor.execute(query)
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
