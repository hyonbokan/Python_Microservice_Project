FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables (example)
ENV PYTHONUNBUFFERED=1

# Expose API Gateway port (change if needed)
EXPOSE 8000

# Run the GraphQL API Gateway
CMD ["python", "gateway/graphql_gateway.py"]
