import requests
import time

url = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'



while(True):
    respuesta = requests.get(url)
    data = respuesta.json()['data']['rates']['EUR']
    print(data)
    time.sleep(10)