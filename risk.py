def calculate_position_size(balance, risk_percent):
    """
    Calculates position size based on account balance and risk.
    """
    risk_amount = balance * risk_percent
    return risk_amount
