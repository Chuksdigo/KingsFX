
import pandas as pd 
from datetime import datetime
import requests
import json


def transform_data():

# read the json file
    with open('./opt/airflow/raw/extract.json', 'r') as json_file:
        response = json.load(json_file)

    rates= []
    timestamp = response['timestamp']

    for rate in response['to']:
        rates.append((timestamp, 'USD', rate['quotecurrency'], rate['mid']))


    df = pd.DataFrame(rates, columns= ['timestamp', 'currency_from', 'currency_to', 'rate'])

   # Cleaning the timestamp column
    df['timestamp'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ"))

    # save to csv
    df.to_csv('./opt/airflow/raw/df.csv', index=False)
    