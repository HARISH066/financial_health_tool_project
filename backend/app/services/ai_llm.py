import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


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

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 300
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=60)
    response.raise_for_status()

    raw_output = response.json()["response"].strip()

    # 🔴 CRITICAL FIX: STRIP MARKDOWN FIRST
    if raw_output.startswith("```"):
        raw_output = raw_output.replace("```json", "")
        raw_output = raw_output.replace("```", "")
        raw_output = raw_output.strip()

    # 🔴 PARSE AFTER SANITIZATION
    try:
        return json.loads(raw_output)
    except Exception:
        return {
            "summary": raw_output,
            "risks": [],
            "cost_optimization": [],
            "financial_products": [],
            "next_steps": []
        }
