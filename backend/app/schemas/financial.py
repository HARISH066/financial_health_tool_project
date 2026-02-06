from pydantic import BaseModel

class FinancialMetrics(BaseModel):
    revenue: float
    expenses: float
    profit: float
    cash_flow_ratio: float
    profit_margin: float


class HealthAssessment(BaseModel):
    score: float
    risk: str


class AIInsightResponse(BaseModel):
    insights: str
