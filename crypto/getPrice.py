import requests


def bitcoin():
    btc_price_url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    t = requests.get(btc_price_url)
    price = t.json()['data']['amount']
    return price


def ethereum():
    eth_price_url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    t = requests.get(eth_price_url)
    price = t.json()['data']['amount']
    return price


def customPrice(ticker):
    try:
        custom_price_url = f"https://api.coinbase.com/v2/prices/{str(ticker)}-USD/spot"
        t = requests.get(custom_price_url)
        price = t.json()['data']['amount']
    except:
        return "Invalid ticker."
    return price
