def place_order(exchange, symbol, side, amount):
    try:
        order = exchange.create_market_order(
            symbol=symbol,
            side=side,
            amount=amount
        )
        return order

    except Exception as e:
        print("Order failed:", e)
        return None
