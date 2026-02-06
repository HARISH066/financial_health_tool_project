from fastapi import APIRouter, HTTPException
from app.schemas.financial import FinancialMetrics
from app.services.scoring import calculate_financial_health
from app.database import SessionLocal
from app.models.assessment import Assessment

router = APIRouter()


@router.post("/assess")
def assess(metrics: FinancialMetrics):
    db = SessionLocal()
    try:
        # 1. Business logic
        result = calculate_financial_health(metrics.dict())

        # 2. Persist to DB
        record = Assessment(
            score=result["score"],
            risk=result["risk"]
        )
        db.add(record)
        db.commit()
        db.refresh(record)

        return result

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()
