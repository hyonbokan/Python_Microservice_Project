import json
import asyncio
import pika
from utils.config import Config
from utils.interfaces import MessageQueueService

class RabbitMQService(MessageQueueService):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=Config.RABBITMQ_HOST,
                port=Config.RABBITMQ_PORT
            )
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=Config.RABBITMQ_QUEUE)
    
    def publish_message(self, message: dict):
        self.channel.basic_publish(
            exchange="",
            routing_key=Config.RABBITMQ_QUEUE,
            body=json.dumps(message),
            properties=pika.BasicProperties(content_type="application/json")
        )
        
    def listen(self, callback):
        self.channel.basic_consume(
            queue=Config.RABBITMQ_QUEUE,
            on_message_callback=callback,
            auto_ack=True
        )
        print("Started listening on RabbitMQ...")
        self.channel.start_consuming()
    
    def close(self):
        self.connection.close()