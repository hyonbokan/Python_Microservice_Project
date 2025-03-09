import asyncio
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from graphql import graphql_sync, build_schema

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
    return "market data service response"

def resolve_get_transaction_data():
    return "transaction service response"

def resolve_get_analytics_data():
    return "analytics service response"


# mapping queries to resolvers
query_resolvers = {
    "getMarketData": resolve_get_market_data,
    "getTransactionData": resolve_get_transaction_data,
    "getAnalyticsData": resolve_get_analytics_data,
}

class GraphQLHander(BaseHTTPRequestHandler):
    def do_POST(self):
        pass