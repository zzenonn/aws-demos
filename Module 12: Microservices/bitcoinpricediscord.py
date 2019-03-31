import requests
import json
import os

baseURL = os.environ['BASEURL']

def lambda_handler(event, context):

    # Get the BTC price from CoinDesk
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(bitcoin_price_url)
    data = response.json()
    price_in_usd = data['bpi']['USD']['rate']
    timestamp = data['time']['updated']
    
    # Post the message to the webhook
    message = "Bitcoin price is currently at $" + price_in_usd + " USD as of " + timestamp
    
    headers = { "Content-Type":"application/json", }

    POSTedJSON =  json.dumps ( {"content":message} )

    r = requests.post(baseURL, headers = headers, data = POSTedJSON)