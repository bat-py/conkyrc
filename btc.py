import requests

usd = float(requests.get('https://blockchain.info/tobtc?currency=USD&value=1').text)
btc  = 1/usd
print(round(btc, 2),'$')
