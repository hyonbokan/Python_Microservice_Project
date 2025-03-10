import asyncio
import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from graphql import graphql_sync, build_schema
from utils.config import Config


# GraphQL schema
graphql_schema = build_schema(
    """
    type Query {
        getMarketData: String
        getTransactionData: String
        getAnalyticsData: String
    }
    """
)

def resolve_get_market_data():
    try:
        response = requests.get(f"http://{Config.POSTGRES_HOST}:5000/market-data")
        return response.json().get("data", "No data available")
    except requests.exceptions.RequestException:
        return "Market data service unavailable"

def resolve_get_transaction_data():
    try:
        response = requests.get(f"http://{Config.POSTGRES_HOST}:5001/transaction-data")
        return response.json().get("data", "No data available")
    except requests.exceptions.RequestException:
        return "transaction service response"

def resolve_get_analytics_data():
    try:
        response = requests.get(f"http://{Config.POSTGRES_HOST}:5002/analytics-data")
        return response.json().get("data", "No data available")
    except requests.exceptions.RequestException:
        return "Analytics data service unavailable"


# mapping queries to resolvers
query_resolvers = {
    "getMarketData": resolve_get_market_data,
    "getTransactionData": resolve_get_transaction_data,
    "getAnalyticsData": resolve_get_analytics_data,
}

class GraphQLHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        request = json.load(post_data.decode('utf-8'))
        
        query = request.get("query")
        variables = request.get("variables", {})
        
        result = graphql_sync(
            graphql_schema, query, root_value=query_resolvers, variables_values=variables
        )
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(result.data).encode())
        

async def start_server():
    server = HTTPServer(("0.0.0.0", 8000), GraphQLHandler)
    print("\nGraphQL API Gateway running on port 8000\n")
    server.serve_forever()
    
if __name__ == "__main__":
    asyncio.run(start_server())