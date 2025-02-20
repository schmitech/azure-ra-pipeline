from azure.eventhub import EventHubConsumerClient
from ..config import Config
import json
import logging
import asyncio
from azure.eventhub.exceptions import EventHubError

class EventHubHandler:
    def __init__(self):
        self.connection_string = Config.EVENTHUB_CONNECTION_STRING
        self.consumer_group = "$Default"
        self.eventhub_name = "risk-events"
        self.max_retries = 3
        self.retry_delay = 1  # seconds
        
    async def receive_with_retry(self, partition_context, event):
        """Process events with retry logic"""
        retries = 0
        while retries < self.max_retries:
            try:
                event_data = json.loads(event.body_as_str())
                logging.info(f"Received event: {event_data}")
                # Process event data here
                await partition_context.update_checkpoint(event)
                return
            except Exception as e:
                retries += 1
                if retries == self.max_retries:
                    logging.error(f"Failed to process event after {retries} retries: {str(e)}")
                    raise
                await asyncio.sleep(self.retry_delay * retries)

    async def start_receiving(self):
        """Start receiving events"""
        client = EventHubConsumerClient.from_connection_string(
            self.connection_string,
            consumer_group=self.consumer_group,
            eventhub_name=self.eventhub_name,
        )
        async with client:
            await client.receive(
                on_event=self.receive_with_retry,
                starting_position="-1"  # Start from end of stream
            ) 