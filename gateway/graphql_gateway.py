import asyncio
import json
import aiohttp
from http.server import BaseHTTPRequestHandler, HTTPServer
from graphql import graphql_sync, build_schema
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
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

# Async helper function to perform GET request
async def async_fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get("data", "No data available")


def resolve_get_market_data():
    try:
        url = f"http://{Config.POSTGRES_HOST}:5000/market-data"
        return asyncio.run(async_fetch(url))
    except Exception as e:
        return "Market data service unavailable"

def resolve_get_transaction_data():
    try:
        url = f"http://{Config.POSTGRES_HOST}:5001/transaction-data"
        return asyncio.run(async_fetch(url))
    except Exception as e:
        return "Transaction service unavailable"
    
def resolve_get_analytics_data():
    try:
        url = f"http://{Config.POSTGRES_HOST}:5002/analytics-data"
        return asyncio.run(async_fetch(url))
    except Exception as e:
        return "Analytics data service unavailable"


# mapping queries to resolvers
query_resolvers = {
    "getMarketData": resolve_get_market_data,
    "getTransactionData": resolve_get_transaction_data,
    "getAnalyticsData": resolve_get_analytics_data,
}

class GraphQLHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        try:
            request = json.loads(post_data.decode("utf-8"))
        except Exception:
            self.send_response(400)
            self.end_headers()
            return
        
        query = request.get("query")
        variables = request.get("variables", {})
        result = graphql_sync(
            graphql_schema, query, root_value=query_resolvers, variable_values=variables
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