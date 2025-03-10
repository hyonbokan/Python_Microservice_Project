# Microservice Project with Python
This project is a **microservices-based architecture** built with Python. It integrates multiple services such as **GraphQL API Gateway, Market Data Service, Transaction Service, Analytics Service, RabbitMQ for messaging, PostgreSQL for database, and Redis for caching.**

---

## 📂 **Project Structure**
```plaintext
📁 Python_Microservice_Project/
├── gateway/         → GraphQL API Gateway (Handles client requests)
├── market_data/     → Market Data Service (Fetches and processes market data)
├── transactions/    → Transaction Service (Handles trade transactions)
├── analytics/       → Price Analytics Service (Performs analytics on market data)
├── message_queue/   → RabbitMQ/Kafka Integration (Handles messaging)
├── database/        → PostgreSQL ORM Layer (Manages database models & migrations)
├── cache/           → Redis Integration (Manages caching)
├── utils/           → Shared utilities (config, helpers)
├── docker/          → Dockerfiles for microservices
│   ├── Dockerfile.gateway
│   ├── Dockerfile.market_data
│   ├── Dockerfile.transactions
│   ├── Dockerfile.analytics
│   ├── Dockerfile.rabbitmq
│   ├── Dockerfile.postgres
│   ├── Dockerfile.redis
├── docker-compose.yml
├── requirements.txt
├── README.md
```

## Start the Project
### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up .env Configuration
```bash
# Database Configuration
POSTGRES_DB=microservice_db
POSTGRES_USER=microservice_user
POSTGRES_PASSWORD=securepassword
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Redis Configuration
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0

# RabbitMQ Configuration
RABBITMQ_QUEUE=market_data_queue
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
```

### 3. Start Docker Services
```bash
docker-compose up --build -d
```

### 4. Verify Services Are Running
```bash
docker ps
```