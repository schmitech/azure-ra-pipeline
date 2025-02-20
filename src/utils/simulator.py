import asyncio
import json
import random
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData

class TransactionSimulator:
    def __init__(self, connection_string, eventhub_name):
        self.producer = EventHubProducerClient.from_connection_string(
            connection_string,
            eventhub_name=eventhub_name
        )
        
    async def generate_transaction(self):
        """Generate a realistic test transaction"""
        transaction_types = ["purchase", "transfer", "withdrawal", "deposit"]
        currencies = ["USD", "EUR", "GBP", "JPY"]
        
        return {
            "event_id": f"TX{random.randint(10000, 99999)}",
            "timestamp": datetime.utcnow().isoformat(),
            "data": {
                "type": random.choice(transaction_types),
                "amount": round(random.uniform(10, 10000), 2),
                "currency": random.choice(currencies),
                "source": "web_portal",
                "user_id": f"USER{random.randint(1000, 9999)}",
                "location": {
                    "country": "US",
                    "region": "NY"
                }
            }
        }
    
    async def send_test_transactions(self, count=10, delay=1):
        """Send test transactions to Event Hub"""
        async with self.producer:
            for _ in range(count):
                transaction = await self.generate_transaction()
                event_data = EventData(json.dumps(transaction))
                await self.producer.send_batch([event_data])
                print(f"Sent transaction: {transaction['event_id']}")
                await asyncio.sleep(delay) 