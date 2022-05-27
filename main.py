from kucoin.client import Market
client = Market(url='https://api.kucoin.com')
klines = client.get_symbol_list()
print(len(klines))

