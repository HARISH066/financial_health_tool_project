from fastapi import FastAPI
from app.routers import assessment, insights, upload, analyse
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

# Import models so SQLAlchemy knows them
from app.models.assessment import Assessment

app = FastAPI(
    title="Financial Health Assessment Tool",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(upload.router)
app.include_router(assessment.router)
app.include_router(insights.router)
app.include_router(analyse.router)


@app.get("/")
def health_check():
    return {"status": "Backend running successfully"}
