import psycopg2
import os

def insert_csv():
    conn = psycopg2.connect(dbname='development',
                            host='localhost',
                            user='postgres',
                            password='password',
                            port='5432')

    conn.autocommit = True

    cur = conn.cursor()

    file_root = '../data/downloads/ons/metadata'

    folder = os.listdir(file_root)

    for file in folder:
        if file[:9] == 'datasets_':
            sql = f"""copy ons_raw._datasets_metadata
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""
            cur.execute(sql)


insert_csv()