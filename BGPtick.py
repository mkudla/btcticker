#!/usr/bin/env python
import requests
import json
import datetime

GDAXethbtc = 'https://api.gdax.com/products/ETH-BTC/book'
GDAXethusd = 'https://api.gdax.com/products/ETH-USD/book'
GDAXbtcusd = 'https://api.gdax.com/products/BTC-USD/book'

r = requests.get(GDAXbtcusd)
json_data = r.json()
GDAXbid_btc_usd = float(json_data["bids"][0][0])
GDAXask_btc_usd = float(json_data["asks"][0][0])
r = requests.get(GDAXethusd)
json_data = r.json()
GDAXbid_eth_usd = float(json_data["bids"][0][0])
GDAXask_eth_usd = float(json_data["asks"][0][0])
r = requests.get(GDAXethbtc)
json_data = r.json()
GDAXbid_eth_btc = float(json_data["bids"][0][0])
GDAXask_eth_btc = float(json_data["asks"][0][0])


POLObigticker = 'https://poloniex.com/public?command=returnTicker'

a = requests.get(POLObigticker)

json_data = a.json()
POLObid_btc_usd = float(json_data["USDT_BTC"]["highestBid"])
POLOask_btc_usd = float(json_data["USDT_BTC"]["lowestAsk"])

POLObid_eth_usd = float(json_data["USDT_ETH"]["highestBid"])
POLOask_eth_usd = float(json_data["USDT_ETH"]["lowestAsk"])

POLObid_eth_btc = float(json_data["BTC_ETH"]["highestBid"])
POLOask_eth_btc = float(json_data["BTC_ETH"]["lowestAsk"])

def prn(x):
  return str("{:7.5f}".format(x))

def prb(x):
  return str("{:6.2f}".format(x))

print
print "DATE:", datetime.datetime.now()
print
print "BTC/ETH"
print "\t\tGDAX\t\tPOLO"
print "SELL : ","\t", prn(GDAXask_eth_btc), "\t", prn(POLOask_eth_btc)
print "BUY  : ","\t", prn(GDAXbid_eth_btc), "\t", prn(POLObid_eth_btc)
print "---"
print "BTC/USD"
print "\t\tGDAX\t\tPOLO"
print "SELL : ","\t", prb(GDAXask_btc_usd), "\t", prb(POLOask_btc_usd)
print "BUY  : ","\t", prb(GDAXbid_btc_usd), "\t", prb(POLObid_btc_usd)
print "---"
print "ETH/USD"
print "\t\tGDAX\t\tPOLO"
print "SELL :","\t\t", prb(GDAXask_eth_usd), "\t\t", prb(POLOask_eth_usd)
print "BUY  :","\t\t", prb(GDAXbid_eth_usd), "\t\t", prb(POLObid_eth_usd)

