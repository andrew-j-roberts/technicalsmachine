import strategies
import update_pairs
from binance.client import Client

client = Client("", "")
candles = strategies.get_candles(client, "IOTABTC", Client.KLINE_INTERVAL_15MINUTE)
price = strategies.get_price(client, "IOTABTC")
bb_strategy = strategies.bb_strategy(client, "IOTABTC", Client.KLINE_INTERVAL_4HOUR)

print(update_pairs.update_pairs_BINANCE())