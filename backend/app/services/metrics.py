def extract_metrics(df):
    # normalize column names
    df.columns = [c.strip().lower() for c in df.columns]

    revenue_keywords = ["revenue", "sales", "turnover", "income"]
    expense_keywords = ["expense", "cost", "expenditure"]
    profit_keywords = ["profit", "net_profit", "income"]

    def sum_matching_columns(keywords):
        matched_cols = [c for c in df.columns if any(k in c for k in keywords)]
        return df[matched_cols].sum().sum() if matched_cols else 0

    revenue = sum_matching_columns(revenue_keywords)
    expenses = sum_matching_columns(expense_keywords)
    profit = sum_matching_columns(profit_keywords)

    # fallback profit calculation
    if profit == 0 and revenue and expenses:
        profit = revenue - expenses

    profit_margin = round(profit / revenue, 2) if revenue else 0
    cash_flow_ratio = round(revenue / expenses, 2) if expenses else 0

    return {
        "revenue": float(revenue),
        "expenses": float(expenses),
        "profit": float(profit),
        "profit_margin": profit_margin,
        "cash_flow_ratio": cash_flow_ratio
    }
