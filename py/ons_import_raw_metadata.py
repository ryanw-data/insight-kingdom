import os
import utils

file_root = '../data/downloads/ons/metadata'

folder = os.listdir(file_root)
def import_datasets():

    cur = utils.db_cursor()

    for file in folder:
        if file[:9] == 'datasets_':
            sql = f"""copy ons_raw._datasets
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor = cur, sql = sql, sql_tag = "datasets import")

    cur.close()

def import_dataset_contacts():

    cur = utils.db_cursor()

    for file in folder:
        if file[:17] == 'dataset_contacts_':
            sql = f"""copy ons_raw._dataset_contacts
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor = cur, sql = sql, sql_tag = "dataset contacts import")

    cur.close()

def import_dataset_keywords():

    cur = utils.db_cursor()

    for file in folder:
        if file[:17] == 'dataset_keywords_':
            sql = f"""copy ons_raw._dataset_keywords
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor = cur, sql = sql, sql_tag = "dataset keywords import")

    cur.close()

def import_dataset_relations():

    cur = utils.db_cursor()

    for file in folder:
           if file[:25] == 'dataset_related_datasets_':
            sql = f"""copy ons_raw._dataset_relations
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor=cur, sql=sql, sql_tag="dataset relations import")

    cur.close()

def import_dataset_methodology():

    cur = utils.db_cursor()

    for file in folder:
           if file[:22] == 'dataset_methodologies_':
            sql = f"""copy ons_raw._dataset_methodology
                      from '/pgData/downloads/ons/metadata/{file}'
                      csv header delimiter ',' null 'null';"""

            utils.sql_runner(cursor=cur, sql=sql, sql_tag="dataset methodology import")

    cur.close()