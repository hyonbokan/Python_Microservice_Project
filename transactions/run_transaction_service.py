import asyncio
from aiohttp import web
from datetime import datetime, timezone
from database.transactions_postgres_service import PostgreSQLTransactionService
from transaction_service import TransactionService
from message_queue.rabbitmq_service import RabbitMQService

database = PostgreSQLTransactionService()
publisher = RabbitMQService()
transaction_service = TransactionService(database=database, publisher=publisher)

async def get_transaction_data(request):
    data = await transaction_service.get_transaction_data()
    return web.json_response({"data": data})

async def create_transaction(request):
    try:
        body = await request.json()
        order_id = body.get("order_id")
        product = body.get("product")
        quantity = body.get("quantity")
        price = body.get("price")
        status = body.get("status", "pending")
        timestamp = datetime.now(timezone.utc).replace(tzinfo=None)
        await transaction_service.create_transaction(order_id, product, quantity, price, status, timestamp)
        return web.json_response({"message": "Transaction created"}, status=201)
    
    except Exception as e:
        return web.json_response({"error": str(e)}, status=400)
    
async def init_app():
    app = web.Application()
    app.router.add_get('/transaction-data', get_transaction_data)
    app.router.add_post('/transaction-data', create_transaction)
    return app

if __name__ == "__main__":
    app = asyncio.run(init_app())
    web.run_app(app, host="0.0.0.0", port=5002)