def forecast_cash_flow(metrics):
    """
    Forecast cash flow based on profit.
    Uses simple average distribution for demo purposes.
    """

    profit = metrics.get("profit", 0)

    if not isinstance(profit, (int, float)):
        profit = 0

    base_cash_flow = round(profit / 3, 2)

    return [
        {"month": "Month 1", "expected_cash_flow": base_cash_flow},
        {"month": "Month 2", "expected_cash_flow": base_cash_flow},
        {"month": "Month 3", "expected_cash_flow": base_cash_flow},
    ]
