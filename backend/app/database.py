import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use PostgreSQL in production, SQLite for local development
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./financial_health.db")

# Fix for Render PostgreSQL URL (postgres:// -> postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Configure engine based on database type
if "sqlite" in DATABASE_URL:
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    # PostgreSQL configuration
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
