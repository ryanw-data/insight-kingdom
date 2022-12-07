import psycopg2
from datetime import datetime
import csv

def create_csv_from_list(list,csv_keys,csv_path,csv_name):

    with open(csv_path + csv_name, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, csv_keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)

    print("Success {0} created!".format(csv_name))


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

    try:

        print(f'Execution of {sql_tag}, starting at {date_time_obj}')

        cursor.execute(sql)

        date_time_obj = datetime.now()

        print(f'Execution of {sql_tag} successful, completed at {date_time_obj}')

    except:

        print(f'Failed to run {sql_tag}')

    return cursor.statusmessage