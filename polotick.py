#!/usr/bin/env python
import requests
import json
import datetime
import logging

#logging.basicConfig(filename='BGtickerdata.log',level=logging.DEBUG)
#loffing.warning('oh no')
#logging.debug('This message should go to the log file')
#logging.info('So should this')

BTCEethbtc = 'https://btc-e.com/api/2/eth_btc/ticker'
BTCEethusd = 'https://btc-e.com/api/2/eth_usd/ticker'
BTCEbtcusd = 'https://btc-e.com/api/2/btc_usd/ticker'

GDAXethbtc = 'https://api.gdax.com/products/ETH-BTC/book'
GDAXethusd = 'https://api.gdax.com/products/ETH-USD/book'
GDAXbtcusd = 'https://api.gdax.com/products/BTC-USD/book'



r = requests.get(GDAXbtcusd)


POLObigticker = 'https://poloniex.com/public?command=returnTicker'


a = requests.get(POLObigticker)

json_data = a.json()
POLObid_btc_usd = json_data["USDT_BTC"]["highestBid"]
POLOask_btc_usd = json_data["USDT_BTC"]["lowestAsk"]

POLObid_eth_usd = json_data["USDT_ETH"]["highestBid"]
POLOask_eth_usd = json_data["USDT_ETH"]["lowestAsk"]

POLObid_btc_eth = json_data["BTC_ETH"]["highestBid"]
POLOask_btc_eth = json_data["BTC_ETH"]["lowestAsk"]

print POLOask_btc_eth

#print a.json()


