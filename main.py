import time
import pandas as pd

from exchange import get_exchange
from strategy import add_indicators, generate_signal
from executor import place_order
from risk import calculate_position_size
from config import SYMBOL, TIMEFRAME, RISK_PER_TRADE


exchange = get_exchange()


def fetch_data():
    ohlcv = exchange.fetch_ohlcv(SYMBOL, timeframe=TIMEFRAME, limit=200)

    df = pd.DataFrame(ohlcv, columns=[
        "timestamp", "open", "high", "low", "close", "volume"
    ])

    return df


while True:
    try:
        df = fetch_data()
        df = add_indicators(df)

        signal = generate_signal(df)

        balance = exchange.fetch_balance()["total"]["USDT"]
        amount = calculate_position_size(balance, RISK_PER_TRADE)

        if signal:
            print("Signal:", signal)

            order_side = "buy" if signal == "buy" else "sell"

            order = place_order(exchange, SYMBOL, order_side, amount)

            print("Order executed:", order)

        else:
            print("No trade")

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(10)
