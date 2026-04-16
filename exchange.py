mport ccxt
from config import BINANCE_API_KEY, BINANCE_API_SECRET

def get_exchange():
    exchange = ccxt.binance({
        "apiKey": BINANCE_API_KEY,
        "secret": BINANCE_API_SECRET,
        "enableRateLimit": True,
        "options": {
            "defaultType": "future"
        }
    })

    return exchange
