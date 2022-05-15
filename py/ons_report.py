import requests
import pandas as pd


def datasets():
    r = requests.get("https://api.beta.ons.gov.uk/v1/datasets?limit=1000&offset=0").json()

    df = pd.DataFrame.from_dict(r['items'])

    file_path = '/Users/ryanwyatt/python/projects/insight_kingdom/data/downloads/ONS/'

    df.to_csv(file_path + 'datasets.csv')

    return df


def get_ons_report(report_name):
    base_url = 'https://api.beta.ons.gov.uk/v1/datasets/'

    r = requests.get(base_url + report_name).json()

    latest_report_url = r['links']['latest_version']['href']

    data = requests.get(latest_report_url).json()

    payload = {
        'dataset_id': data['id'],
        'dataset_name': data['links']['dataset']['id'],
        'dataset_collection_id': data['collection_id'],
        'dataset_url': data['links']['dataset']['href'],
        'csv_download_url': data['downloads']['csv']['href'],
        'release_date': data['release_date'],
        'full_response': data
    }

    return payload

datasets()

