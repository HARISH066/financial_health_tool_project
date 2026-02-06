import requests
import json
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "gemma3:4b")


def generate_ai_insights(metrics, assessment, credit, forecast, benchmark, language="English"):
    prompt = f"""
You are a financial advisor for small and medium enterprises.

Respond STRICTLY in valid JSON.
DO NOT use markdown.
DO NOT wrap the response in ```json or ```.

Return ONLY raw JSON.

Respond in {language}.

JSON FORMAT:
{{
  "summary": "2–3 sentence summary",
  "risks": ["risk 1", "risk 2"],
  "cost_optimization": ["suggestion 1", "suggestion 2"],
  "financial_products": ["product 1", "product 2"],
  "next_steps": ["step 1", "step 2", "step 3"]
}}

BUSINESS DATA:
Revenue: {metrics['revenue']}
Expenses: {metrics['expenses']}
Profit: {metrics['profit']}
Profit Margin: {metrics['profit_margin']}
Cash Flow Ratio: {metrics['cash_flow_ratio']}

Financial Health Score: {assessment['score']}
Risk Level: {assessment['risk']}

Loan Eligibility: {credit['loan_eligibility']}
Risk Flags: {credit['risk_flags']}

Industry: {benchmark['industry']}
Profit Margin Status: {benchmark['profit_margin_status']}
Cash Flow Status: {benchmark['cash_flow_status']}

Forecast:
{forecast}
"""

    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.3,
                "num_predict": 300
            }
        }

        response = requests.post(OLLAMA_URL, json=payload, timeout=10)
        response.raise_for_status()

        raw_output = response.json()["response"].strip()

        # Strip markdown if present
        if raw_output.startswith("```"):
            raw_output = raw_output.replace("```json", "")
            raw_output = raw_output.replace("```", "")
            raw_output = raw_output.strip()

        return json.loads(raw_output)
    
    except Exception as e:
        # Return fallback insights if LLM is not available
        print(f"AI LLM not available: {e}")
        return generate_fallback_insights(metrics, assessment, credit, benchmark)


def generate_fallback_insights(metrics, assessment, credit, benchmark):
    """Generate rule-based insights when LLM is not available"""
    
    summary = f"Your business shows a financial health score of {assessment['score']}/100 with {assessment['risk'].lower()} risk. "
    
    if metrics['profit_margin'] > 0.2:
        summary += "Strong profit margins indicate good operational efficiency. "
    else:
        summary += "Profit margins could be improved through cost optimization. "
    
    if credit['loan_eligibility'] == "Eligible":
        summary += "You are eligible for business loans."
    
    risks = []
    if assessment['risk'] == "High":
        risks.append("High financial risk detected - immediate action needed")
    if metrics['profit_margin'] < 0.15:
        risks.append("Low profit margin - review pricing and costs")
    if metrics['cash_flow_ratio'] < 1:
        risks.append("Negative cash flow - monitor liquidity closely")
    if not risks:
        risks.append("No major risks identified - maintain current practices")
    
    cost_optimization = []
    if metrics['expenses'] > metrics['revenue'] * 0.7:
        cost_optimization.append("Review and reduce operational expenses")
        cost_optimization.append("Negotiate better rates with suppliers")
    else:
        cost_optimization.append("Maintain current cost structure")
        cost_optimization.append("Look for economies of scale opportunities")
    
    financial_products = []
    if credit['loan_eligibility'] == "Eligible":
        financial_products.append("Working capital loan for business expansion")
        financial_products.append("Business line of credit for flexibility")
    elif credit['loan_eligibility'] == "Conditionally Eligible":
        financial_products.append("Secured business loan with collateral")
        financial_products.append("Invoice financing for cash flow")
    else:
        financial_products.append("Focus on improving financial metrics first")
        financial_products.append("Consider microfinance or peer-to-peer lending")
    
    next_steps = [
        "Monitor cash flow weekly to ensure liquidity",
        "Review and optimize major expense categories",
        "Set quarterly financial targets and track progress"
    ]
    
    if benchmark['profit_margin_status'] == "Below Average":
        next_steps.append(f"Work to improve profit margin to industry average of {benchmark['industry_avg_profit_margin']}")
    
    return {
        "summary": summary,
        "risks": risks,
        "cost_optimization": cost_optimization,
        "financial_products": financial_products,
        "next_steps": next_steps
    }
