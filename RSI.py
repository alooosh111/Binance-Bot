import websocket, json, pprint, talib, numpy
from binance.client import Client
from binance.enums import *
import config


RSI_PERIOD = 14
RSI_OVERBOUGHT = int(input(" Enter The Over Bought Value :"))
RSI_OVERSOLD = int(input("Enter The Over Soled Value :"))
TRADE_SYMBOL = input("The Pair U Want To Trade In Apper Case : ")
TRADE_QUANTITY = 0.05
STOP_LOSS = 30
API_KEY = config.API_KEY
API_SECRET = config.API_SECRET
The_Socket_Data = input("Enter The Pair U Want To Trade in Lower Case: ")
The_Frame = input("Enter The Time Frame U Want Trade In: ")


SOCKET = "wss://stream.binance.com:9443/ws/"+The_Socket_Data+"@kline_"+The_Frame+"m"

client = Client(API_KEY, API_SECRET)

print(Client)

info = Client.get_account()
print(info)
