# Virtual environment directory
VENV=venv
PYTHON=python3

.PHONY: venv install run-gateway run-market queue start-services clean

# 1. Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created."

# 2. Install dependencies
install: venv
	$(VENV)/bin/pip install -r backend/requirements.txt
	@echo "Dependencies installed."

# 3. Run the GraphQL API Gateway
run-gateway:
	$(VENV)/bin/python backend/gateway/graphql_gateway.py

# 4. Run the Market Data Service
run-market:
	$(VENV)/bin/python backend/market_data/run_market_data.py

# 5. Run RabbitMQ listener service
queue:
	$(VENV)/bin/python backend/message_queue/rabbitmq_service.py

# 6. Run database migration
migrate:
	alembic upgrade head

# 7. Generate a new migration
new-migration:
	alembic revision --autogenerate -m "New changes"

# 8. Clean project
clean:
	rm -rf $(VENV)
	@echo "Cleaned project: virtual environment removed."