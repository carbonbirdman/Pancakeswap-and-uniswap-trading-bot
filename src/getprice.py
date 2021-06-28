#!python
import datetime
from itertools import permutations
import time
from swap import Uniswap
from web3 import Web3, middleware, _utils
from web3.gas_strategies.time_based import fast_gas_price_strategy, glacial_gas_price_strategy
from pycoingecko import CoinGeckoAPI
#from worker import Worker
import pyetherbalance
import requests
import math
import subprocess
import sys
import fileinput
import re
import importlib
import os
from time import localtime, strftime
from web3 import types
import traceback
import configfile
import json
import requests

sys.path.insert(0, './')
sys.path.append(".")
sys.setrecursionlimit(1500)

cg = CoinGeckoAPI()
importlib.reload(configfile)

w3 = Web3()

#app = main_loop(sys.argv)
maxgwei = int(configfile.maxgwei)
maxgweinumber = int(configfile.maxgweinumber)
timesleepaftertrade = int(configfile.secondscheckingprice_2)
timesleep = int(configfile.secondscheckingprice)
infura_url = str(configfile.infuraurl)
infuraurl = infura_url
tokentokennumerator = float(configfile.tokentokennumerator)
from secrets import my_address
ethereum_address = my_address

# Settings for BNB
ethaddress = "0x0000000000000000000000000000000000000000"
maindecimals = 18
token_address = "0xe9e7cea3dedca5984780bafc599bd69add087d56"

# Get coin price
# turn this into function
#price = get_coin_price(all_token_information, infura_url, ethaddress, maindecimals, my_address)
ethbalance = pyetherbalance.PyEtherBalance(infura_url)
pricefeed = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT').json()['price']
priceeth = int(float(pricefeed))
balance_eth = ethbalance.get_eth_balance(my_address)['balance']
dollarbalancemaintoken = priceeth * balance_eth
#maintokeneth = uniswap_wrapper.get_eth_token_input_price(w3.toChecksumAddress(ethaddress),100)

with open(f"router02.abi") as f:
    abi = json.load(f)
contract_address = "0x0eD7e52944161450477ee417DE9Cd3a859b14fD0"
contract_address = w3.toChecksumAddress(token_address)
weth_address = w3.toChecksumAddress('0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c')
router = w3.eth.contract(address=contract_address, abi=abi)
maintoken_eth = router.functions.getAmountsOut(100, [weth_address, w3.toChecksumAddress(token_address)]).call()

#mainusd = (priceeth / (maintokeneth)) * 100
#print(mainusd * balance_eth)
#token_eth = uniswap_wrapper.get_eth_token_input_price(w3.toChecksumAddress(token_address),10000000000000)
#pricetoken1usd = (priceeth / (token1eth))

