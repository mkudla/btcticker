#!/usr/bin/env python
import requests
import json
import datetime
import logging

logging.basicConfig(filename='BGtickerdata.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')

BTCEethbtc = 'https://btc-e.com/api/2/eth_btc/ticker'
BTCEethusd = 'https://btc-e.com/api/2/eth_usd/ticker'
BTCEbtcusd = 'https://btc-e.com/api/2/btc_usd/ticker'

GDAXethbtc = 'https://api.gdax.com/products/ETH-BTC/book'
GDAXethusd = 'https://api.gdax.com/products/ETH-USD/book'
GDAXbtcusd = 'https://api.gdax.com/products/BTC-USD/book'

r = requests.get(GDAXbtcusd)
s = requests.get(GDAXethusd)
t = requests.get(GDAXethbtc)



#u = requests.get(BTCEethbtc)
#v = requests.get(BTCEethusd)
#w = requests.get(BTCEbtcusd)

f = open('workfile', 'w')


stringtoprint = r.json(),"\t",r.json(),"\t",s.json(),"\t",t.json()
#,"\t",u.json(),"\t",v.json(),"\t",w.json()
f.write(str(stringtoprint))
f.close()
