from urllib.request import Request, urlopen
import json
import os

slack_webhook_url = os.environ['SLACK_WEBHOOK']


def lambda_handler(event, context):

    # Get the BTC price from CoinDesk
    bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    r = urlopen(bitcoin_price_url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    price_in_usd = data['bpi']['USD']['rate']
    timestamp = data['time']['updated']
    
    # Post the message to the slack webhook
    message = {
        "text": "Bitcoin price is currently at $" + price_in_usd + " USD as of " + timestamp
    }
    
    req = Request(slack_webhook_url, json.dumps(message).encode('utf-8'))
    
    response = urlopen(req)
    response.read()
