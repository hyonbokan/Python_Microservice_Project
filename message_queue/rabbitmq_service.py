import json
import asyncio
import pika
from utils.config import Config
from utils.interfaces import MessageQueueService, DatabaseService

class RabbitMQService(MessageQueueService):
    def __init__(self, db_service: DatabaseService, pika_connection: pika.BlockingConnection):
        self.db_service = db_service
        self.pika_connection = pika_connection
        self.channel = self.pika_connection.channel()
        self.channel.queue_declare(queue=Config.RABBITMQ_QUEUE)
    
    def rabbitmq_callback(self, ch, method, properties, body):
        trade_data = json.loads(body)
        asyncio.run(self.db_service.save_trade_data(
            trade_data['market'],
            trade_data['price'],
            trade_data['timestamp']
        ))
        print(f"Received trade data: {trade_data}")
        
    def listen(self):
        self.channel.basic_consume(
            queue=Config.RABBITMQ_QUEUE,
            on_message_callback=self.rabbitmq_callback,
            auto_ack=True
        )
        print("Listening for market data messages...")
        self.channel.start_consuming()