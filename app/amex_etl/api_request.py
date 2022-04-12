import requests
import json
import yaml
import keyring
from datetime import datetime, timedelta

# Credentials
USERNAME = 'USERNAME'
PASSWORD = keyring.get_password('amex_password', USERNAME)
TOKEN = keyring.get_password('amex_token', USERNAME)

# Get relevant dates
today = datetime.now().strftime('%Y-%m-%d')
week_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

# Load configs
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

session, transactions = (config['session'], config['transactions'])

# Replace sensitive data in configs
session['payload'] = session['payload'].replace('{USERNAME}', USERNAME)
session['payload'] = session['payload'].replace('{PASSWORD}', PASSWORD)
transactions['headers']['account_token'] = transactions['headers']['account_token'].replace('{TOKEN}', TOKEN)


def get_transactions(start_date=week_ago, end_date=today):
    # Replace dates
    transactions['querystring']['start_date'] = start_date
    transactions['querystring']['end_date'] = end_date

    with requests.Session() as s:
    
        # Initial request to establish sesssion and set cookies
        s.request(
            'POST',
            session['url'],
            data=session['payload'],
            headers=session['headers']
        )

        # Main request to get transactions
        response = s.request(
            'GET',
            transactions['url'],
            headers=transactions['headers'],
            params=transactions['querystring']
        ).json()['transactions']
    
    return response

