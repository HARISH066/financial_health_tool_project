from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routers import assessment, insights, upload, analyse
from app.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
import os

# Import models so SQLAlchemy knows them
from app.models.assessment import Assessment

app = FastAPI(
    title="Financial Health Assessment Tool",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for single deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

# API Routers
app.include_router(upload.router)
app.include_router(assessment.router)
app.include_router(insights.router)
app.include_router(analyse.router)

# Serve React frontend (if build exists)
frontend_build_path = os.path.join(os.path.dirname(__file__), "../../frontend/build")
if os.path.exists(frontend_build_path):
    app.mount("/static", StaticFiles(directory=os.path.join(frontend_build_path, "static")), name="static")
    
    @app.get("/")
    def serve_frontend():
        return FileResponse(os.path.join(frontend_build_path, "index.html"))
    
    @app.get("/{full_path:path}")
    def serve_frontend_routes(full_path: str):
        file_path = os.path.join(frontend_build_path, full_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return FileResponse(file_path)
        return FileResponse(os.path.join(frontend_build_path, "index.html"))
else:
    @app.get("/")
    def health_check():
        return {"status": "Backend running successfully"}
