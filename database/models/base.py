from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.config import Config

# Define Async Database URL (shared across models)
DATABASE_URL = f"postgresql+asyncpg://{Config.POSTGRES_USER}:{Config.POSTGRES_PASSWORD}@{Config.POSTGRES_HOST}:{Config.POSTGRES_PORT}/{Config.POSTGRES_DB}"

# Create Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create Async Session Factory
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Base Model
Base = declarative_base()