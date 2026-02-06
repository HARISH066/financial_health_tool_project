from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.ingestion import load_financial_data
from app.services.metrics import extract_metrics
from app.services.scoring import calculate_financial_health
from app.services.ai_insights import generate_insights
from app.database import SessionLocal
from app.models.assessment import Assessment
from app.services.credit import evaluate_creditworthiness
from app.services.forecast import forecast_cash_flow
from app.services.benchmark import benchmark_industry
from app.services.ai_llm import generate_ai_insights





router = APIRouter()

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/analyze-csv")
def analyze_csv(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 1. Load CSV
    df = load_financial_data(file_path)

    # 2. Extract metrics
    metrics = extract_metrics(df)

    # 3. Calculate score
    assessment = calculate_financial_health(metrics)
    
    credit = evaluate_creditworthiness(metrics, assessment)
    
    forecast = forecast_cash_flow(metrics)
    
    benchmark = benchmark_industry(metrics, industry="Retail")
    
    ai_summary = generate_ai_insights(
    metrics=metrics,
    assessment=assessment,
    credit=credit,
    forecast=forecast,
    benchmark=benchmark,
    language="English"  # later: Hindi / Tamil etc.
)





    # 4. Save to DB
    db = SessionLocal()
    record = Assessment(
    score=float(assessment["score"]),
    risk=str(assessment["risk"])
)

    db.add(record)
    db.commit()
    db.close()

    # 5. AI Insights
    insights = generate_insights(assessment)

    return {
    "metrics": metrics,
    "assessment": assessment,
    "creditworthiness": credit,
    "forecast": forecast,
    "benchmark": benchmark,
    "ai_insights": ai_summary
}




