INDUSTRY_BENCHMARKS = {
    "Retail": {
        "profit_margin": 0.20,
        "cash_flow_ratio": 1.2
    },
    "Manufacturing": {
        "profit_margin": 0.18,
        "cash_flow_ratio": 1.3
    },
    "Services": {
        "profit_margin": 0.25,
        "cash_flow_ratio": 1.4
    }
}


def benchmark_industry(metrics, industry="Retail"):
    benchmark = INDUSTRY_BENCHMARKS.get(industry, INDUSTRY_BENCHMARKS["Retail"])

    comparison = {
        "industry": industry,
        "your_profit_margin": metrics["profit_margin"],
        "industry_avg_profit_margin": benchmark["profit_margin"],
        "profit_margin_status": (
            "Above Average"
            if metrics["profit_margin"] >= benchmark["profit_margin"]
            else "Below Average"
        ),
        "your_cash_flow_ratio": metrics["cash_flow_ratio"],
        "industry_avg_cash_flow_ratio": benchmark["cash_flow_ratio"],
        "cash_flow_status": (
            "Healthy"
            if metrics["cash_flow_ratio"] >= benchmark["cash_flow_ratio"]
            else "Weak"
        )
    }

    return comparison
