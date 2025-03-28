from utils.interfaces import TransactionDatabaseService, MessageQueueService

class TransactionService:
    def __init__(self, database: TransactionDatabaseService, publisher: MessageQueueService):
        self.database = database
        self.publisher = publisher
        
    async def get_transaction_data(self):
        return await self.database.fetch_transaction_data()
    
    async def create_transaction(self, order_id, product, quantity, price, status, timestamp):
        await self.database.save_transaction_data(order_id, product, quantity, price, status, timestamp)
        message = {
            "order_id": order_id,
            "product": product,
            "quantity": quantity,
            "price": price,
            "status": status,
            "timestamp": timestamp.isoformat(),
        }
        self.publisher.publish_message(message=message)