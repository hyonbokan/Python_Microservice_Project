import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database Configuration
    POSTGRES_DB = os.getenv("POSTGRES_DB", "microservice_db")
    POSTGRES_USER = os.getenv("POSTGRES_USER", "microservice_user")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password123")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    
    # Redis Configuration
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT"))
    REDIS_DB = int(os.getenv("REDIS_DB"))

    # RabbitMQ Configuration
    RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE")
    RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
    RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT"))