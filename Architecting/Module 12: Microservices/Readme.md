# Microservices

See bitcoinpricediscord.py for a sample lambda function. Assuming you're using a python virtual environment, include the site-packages folder in the zip. You can then run `aws lambda update-function-code --function-name GetBitcoinPrice --zip-file fileb://bitcoinpriceupdates.zip`