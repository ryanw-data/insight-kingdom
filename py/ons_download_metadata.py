import requests
from datetime import datetime
import pandas as pd
import json
import io

def datasets():

    r = requests.get("https://api.beta.ons.gov.uk/v1/datasets?limit=1000&offset=0").json()

    raw_response = r['items']

    datasets = []

    dataset_contacts = []

    dataset_methodologies = []

    dataset_keywords = []

    dataset_related_datasets = []

    for dataset in raw_response:

        dataset_link = dataset.get('links', {}).get('latest_version', {}).get('href', None)

        dataset_link_response = requests.get(dataset_link).json()

        collection_id = dataset_link_response.get('collection_id',None)
        download_link = dataset_link_response.get('downloads',{}).get('csv',{}).get('href',None)
        release_date = dataset_link_response.get('release_date',None)
        usage_notes = dataset_link_response.get('usage_notes',None)

        dataset_item = {
        'dataset_id': dataset.get('id',None),
        'dataset_collection_id': collection_id,
        'dataset_title': dataset.get('title', None),
        'dataset_description': dataset.get('description',None),
        'dataset_state': dataset.get('state',None),
        'dataset_release_date': release_date,
        'dataset_next_release': dataset.get('next_release',None),
        'dataset_release_frequency': dataset.get('release_frequency',None),
        'dataset_national_stastic': dataset.get('national_statistic',None),
        'dataset_type': dataset.get('type',None),
        'dataset_editions_link': dataset.get('links',{}).get('editions',{}).get('href',None),
        'dataset_latest_version_link': dataset.get('links', {}).get('latest_version', {}).get('href', None),
        'dataset_latest_version_id': dataset.get('links', {}).get('latest_version', {}).get('id', None),
        'dataset_download_url': download_link,
        'dataset_self_link': dataset.get('links', {}).get('self', {}).get('href', None),
        'dataset_taxonomy_link': dataset.get('links', {}).get('taxonomy', {}).get('href', None),
        'dataset_quality_methodology_information_link': dataset.get('qmi', {}).get('href', None),
        'dataset_publications': dataset.get('publications',None),
        'dataset_unit_of_measure': dataset.get('unit_of_measure',None),
        'dataset_licence': dataset.get('license',None),
        'dataset_usage_notes': usage_notes
        }

        datasets.append(dataset_item)

        if dataset.get('contacts', None) != None:

            for contact in dataset.get('contacts',None):

                contact_item = {
                    'dataset_id': dataset.get('id',None),
                    'dataset_contact_email': contact.get('email',None),
                    'dataset_contact_name': contact.get('name', None),
                    'dataset_contact_telephone': contact.get('telephone', None)
                }

                dataset_contacts.append(contact_item)

        if dataset.get('methodologies',None) != None:

            for methodology in dataset.get('methodologies'):

                methodology_item = {
                    'dataset_id': dataset.get('id',None),
                    'dataset_methodology_url': methodology.get('email', None),
                    'dataset_methodology_title': methodology.get('name', None)
                }

                dataset_methodologies.append(methodology_item)

        if dataset.get('keywords',None) != None:

            for keyword in dataset.get('keywords',None):

                keyword_item = {
                    'dataset_id': dataset.get('id',None),
                    'dataset_keyword': keyword
                }

                dataset_keywords.append(keyword_item)

        if dataset.get('related_datasets',None) != None:

            for related_dataset in dataset.get('related_datasets',None):

                related_dataset_item = {
                    'dataset_id': dataset.get('id',None),
                    'related_dataset_url': related_dataset.get('href',None),
                    'related_dataset_title': related_dataset.get('title',None)
                }

                dataset_related_datasets.append(related_dataset_item)

    response = {
        'run_date': datetime.now().strftime("%d-%m-%Y-%H-%M-%S"),
        'raw_json': r,
        'payload':
            {
        'datasets': datasets,
        'dataset_contacts': dataset_contacts,
        'dataset_methodologies': dataset_methodologies,
        'dataset_keywords': dataset_keywords,
        'dataset_related_datasets': dataset_related_datasets
            }
    }


    return response

data = datasets()

rundate = data['run_date']

file_path = '../data/downloads/ONS/'

with open(file_path + 'raw_response' + '_' + rundate + '.json', 'w', encoding='utf-8') as f:
    json.dump(data['raw_json'], f, ensure_ascii=False, indent=4)

for file in data['payload']:

    file_df = pd.DataFrame(data['payload'][file])

    file_df.to_csv(file_path + 'metadata/' + file + '_' + rundate + '.csv', index=False)

# for dataset in data['payload']['datasets']:
#
#     download_url = dataset['dataset_download_url']
#     name = dataset['dataset_id']
#
#     dataset_download = requests.get(download_url)
#
#     file_object = io.StringIO(dataset_download.content.decode('utf-8'))
#
#     data_df = pd.read_csv(file_object)
#
#     data_df.to_csv(file_path + name + '_' + rundate + '.csv', index=False)
#
