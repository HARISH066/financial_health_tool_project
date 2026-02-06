from fastapi import APIRouter
from app.services.ai_insights import generate_insights
from app.schemas.financial import HealthAssessment, AIInsightResponse

router = APIRouter()

@router.post("/insights", response_model=AIInsightResponse)
def insights(score_data: HealthAssessment):
    return {
        "insights": generate_insights(score_data.dict())
    }
