from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict, Callable
from datetime import datetime
class CacheService(ABC):
    @classmethod
    @abstractmethod
    def save(cls, key: str, value: Any, expiry: int) -> None:
        pass
    
    @classmethod
    @abstractmethod
    def get(cls, key: str) -> Optional[Any]:
        pass


class MarketDatabaseService(ABC):
    @classmethod
    @abstractmethod
    async def fetch_trade_data(cls) -> List[Dict[str, Any]]:
        pass
    
    @classmethod
    @abstractmethod
    async def save_trade_data(cls, market: str, price: float, timestamp: datetime) -> None:
        pass


class TransactionDatabaseService(ABC):
    @classmethod
    @abstractmethod
    async def fetch_transaction_data(cls) -> List[Dict[str, Any]]:
        pass
    
    
    @classmethod
    @abstractmethod
    async def save_transaction_data(
        cls, order_id: int, 
        product: str, 
        quantity: int, 
        price: float, 
        status: str, 
        timestamp: Any
    ) -> None:
        pass
    
    
class MessageQueueService(ABC):
    @classmethod
    @abstractmethod
    def publish_message(cls, message: dict) -> None:
        pass
    
    @classmethod
    @abstractmethod
    def listen(cls, callback: Callable[[Any], None]) -> None:
        pass