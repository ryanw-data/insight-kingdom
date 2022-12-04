import psycopg2
from datetime import datetime

def db_cursor():

    user = 'postgres'
    password = 'password'

    print(f"Connecting to database with user {user}")

    try:
        conn = psycopg2.connect(dbname='development',
                                host='localhost',
                                user=user,
                                password=password,
                                port='5432')

        conn.autocommit = True

        c = conn.cursor()

        print(f'Connection successful!')

        c.execute("SELECT VERSION()")

        print(c.fetchone())

    except:

        print('Failed to connect')

    return c


def sql_runner(cursor, sql, sql_tag):

    date_time_obj = datetime.now()

    print(f'Execution of {sql_tag}, starting at {date_time_obj}')

    try:
        cursor.execute(sql)

        date_time_obj = datetime.now()
        print(f'Execution of {sql_tag} successful, completed at {date_time_obj}')

    except:

        print(f'Failed to run {sql_tag}')

    return cursor.fetchone()

cur = db_cursor()

result = sql_runner(cur,'SELECT 1','Test')

print(result)

cur.close()
