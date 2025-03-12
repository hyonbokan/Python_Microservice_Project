from abc import ABC, abstractmethod


class CacheService(ABC):
    @classmethod
    @abstractmethod
    def save(self, key, value, expiry):
        pass
    
    @classmethod
    @abstractmethod
    def get(self, key):
        pass


class MarketDatabaseService(ABC):
    @classmethod
    @abstractmethod
    async def fetch_trade_data(self):
        pass
    
    @classmethod
    @abstractmethod
    async def save_trade_data(self, market, price, timestamp):
        pass


class TransactionDatabaseService(ABC):
    @classmethod
    @abstractmethod
    async def fetch_transaction_data(self):
        pass
    
    
    @classmethod
    @abstractmethod
    async def save_transaction_data(self, order_id, product, quantity, price, status, timestamp):
        pass
    
    
class MessageQueueService(ABC):
    @classmethod
    @abstractmethod
    def listen(self):
        pass