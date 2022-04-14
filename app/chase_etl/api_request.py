import requests
import json
import yaml
from datetime import datetime, timedelta

# Session cookie
SESSION = "<SESSION COOKIE HERE>"

# Get relevant dates
date = datetime.now()
default_timeframe = date.strftime('%Y') + date.strftime('%m')

# Load configs
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

accounts, transactions = (config['accounts'], config['transactions'])

# Replace session data in config
accounts['headers']['Cookie'] = accounts['headers']['Cookie'].replace('{SMSESSION}', f"SMSESSION={SESSION}")

def get_accounts():

    # Get account numbers
    try:
        response = requests.request('POST', accounts['url'], headers=accounts['headers'])
        accts = response.json()['cache'][1]['response']['accountTiles']
    except KeyError:
        return response.text

    acct_nums = []
    for a in accts:
        acct_nums.append(str(a['accountId']))

    return acct_nums

def get_transactions(timeframe=default_timeframe):

        accts = get_accounts()

        # Replace data in config
        transactions['querystring']['accounts'] = transactions['querystring']['accounts'].replace('{ACCOUNTS}', ','.join(accts))
        transactions['querystring']['requested-time-frame-type-name'] = transactions['querystring']['requested-time-frame-type-name'].replace('{TIMEFRAME}', timeframe)
        transactions['headers']['Cookie'] = transactions['headers']['Cookie'].replace('{SMSESSION}', f"SMSESSION={SESSION}")

        # Get transactions
        try:
            response = requests.request('GET', transactions['url'], headers=transactions['headers'], params=transactions['querystring'])
            trans = response.json()['transactions']
        except KeyError:
            return response.text

        return trans

results = get_transactions()
print(json.dumps(results, indent=4))
