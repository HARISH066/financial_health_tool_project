def evaluate_creditworthiness(metrics, assessment):
    risk_flags = []

    # Rule 1: Profitability
    if metrics["profit_margin"] < 0.15:
        risk_flags.append("Low profit margin")

    # Rule 2: Cash flow
    if metrics["cash_flow_ratio"] < 1:
        risk_flags.append("Poor cash flow")

    # Rule 3: Overall score
    if assessment["score"] < 40:
        risk_flags.append("Low financial health score")

    # Final decision
    if len(risk_flags) == 0:
        eligibility = "Eligible"
    elif len(risk_flags) == 1:
        eligibility = "Conditionally Eligible"
    else:
        eligibility = "Not Eligible"

    return {
        "loan_eligibility": eligibility,
        "risk_flags": risk_flags
    }
