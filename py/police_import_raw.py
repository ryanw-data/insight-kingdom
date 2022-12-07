import os
import utils

def import_forces():

    file_root = '../data/downloads/police-uk/metadata'

    folder = os.listdir(file_root)

    cur = utils.db_cursor()

    for file in folder:
        if file[:7] == 'forces_':
            sql = f"""copy police_uk_raw.forces
                      from '/pgData/downloads/police-uk/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor = cur, sql = sql, sql_tag = "forces import")

    cur.close()

def import_neighbourhoods():

    file_root = '../data/downloads/police-uk/metadata/neighbourhoods'

    folder = os.listdir(file_root)

    cur = utils.db_cursor()

    for file in folder:
        if file[:15] == 'neighbourhoods_':
            sql = f"""copy police_uk_raw.neighbourhoods
                      from '/pgData/downloads/police-uk/metadata/neighbourhoods/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor = cur, sql = sql, sql_tag = "neighbourhoods import")

    cur.close()