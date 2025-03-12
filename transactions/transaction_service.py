from utils.interfaces import TransactionDatabaseService

class TransactionService:
    def __init__(self, database: TransactionDatabaseService):
        self.database = database
        
    async def get_transaction_data(self):
        return await self.database.fetch_transaction_data()
    
    async def create_transaction(self, order_id, product, quantity, price, status, timestamp):
        await self.database.save_transaction_data(order_id, product, quantity, price, status, timestamp)