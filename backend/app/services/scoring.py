def calculate_financial_health(metrics):
    score = 0

    score += min(metrics["cash_flow_ratio"] * 25, 25)
    score += min(metrics["profit_margin"] * 20, 20)

    risk = "Low" if score > 30 else "High"

    return {
    "score": float(score),
    "risk": str(risk)
}
