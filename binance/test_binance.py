#Test script for binance APIs
import setup
import requests
import json
import pprint

#url and header
url = 'https://api.binance.com'
headers = {'Content-type' : 'application/x-www-form-urlencoded', 'X-MBX-APIKEY' : setup.api_key}

#Query Data
#No param
#data = "/api/v1/exchangeInfo"
data = "/api/v1/time"

#Param Needed
#data = "/api/v1/historicalTrades"
data = "/api/v3/ticker/price"

#Symbols
symbol = "LTCBTC"

#Params
#params = ""
params = {'symbol' : symbol}

#API
response = requests.get(url+data, params,  headers=headers)

#Output
json_r = response.json()
print(json.dumps(json_r, indent=4))

