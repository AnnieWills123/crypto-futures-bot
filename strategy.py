import pandas as pd
import ta


def add_indicators(df):
    df["ema50"] = ta.trend.ema_indicator(df["close"], window=50)
    df["ema200"] = ta.trend.ema_indicator(df["close"], window=200)
    df["rsi"] = ta.momentum.rsi(df["close"], window=14)
    return df


def generate_signal(df):
    last = df.iloc[-1]

    # Trend filter
    bullish = last["ema50"] > last["ema200"]
    bearish = last["ema50"] < last["ema200"]

    # Long condition
    if bullish and 55 <= last["rsi"] <= 65:
        return "buy"

    # Short condition
    if bearish and 35 <= last["rsi"] <= 45:
        return "sell"

    return None
