import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import asyncio
from aiohttp import web
from database.postgres_service import PostgreSQLService
from cache.redis_cache import RedisCacheService

async def market_data_handler(request):
    # Dependency injection
    cache = RedisCacheService()
    db_service = PostgreSQLService(cache=cache)
    
    # Fetch trade data asynchronously
    data = await db_service.fetch_trade_data()
    response_data = {"data": data}
    return web.json_response(response_data)

async def init_app():
    app = web.Application()
    # Route for the market data endpoint
    app.router.add_get('/market-data', market_data_handler)
    return app

if __name__ == "__main__":
    app = asyncio.run(init_app())
    # Run the aiohttp server on host 0.0.0.0 and port 5000
    web.run_app(app, host='0.0.0.0', port=5000)