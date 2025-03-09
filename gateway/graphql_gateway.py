import asyncio
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from graphql import graphql_sync, build_schema