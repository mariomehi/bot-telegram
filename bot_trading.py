import time #libreria ora
import ccxt #libreria trading

#creiamo oggetto exchange e usiamo le api keys del nostro exchange in questo caso Binance
exchange = ccxt.binance({
  'apiKey' : 'stringaPiùCorta'
  'secret' : 'piùLungaMaImportanteTenerlaNascosta'
  'enableRateLimit' : True; #limitatore di traffico
}) #

def quanto_in_dollari(cosa,quanto):
return quanto/exchange.fetchTicker(cosa+'/USDT')['last'] #last -> etichetta del dizionario
#print(prezzo_attuale) restituisce una stringa del prezzo dell'asset

#compro in modalità spot a mercato
exchange.createMarketBuyOrder('BTC/USDT', quanto_in_dollari('BTC',20)) #compro 20$ a mercato

#vendo in modalità spot a mercato
exchange.createMarketSellOrder('BTC/USDT', quanto_in_dollari('BTC',20)) #vendo 20$ a mercato

#piccolo bot telegram per comprare e vendere crypto tramite binance
#verrà aggiornato in futuro
#18 settembre 2021
