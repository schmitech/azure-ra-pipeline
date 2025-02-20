from azure.cosmos import CosmosClient
from ..config import Config
import logging

class CosmosDBClient:
    def __init__(self):
        self.client = CosmosClient(
            Config.COSMOS_ENDPOINT,
            Config.COSMOS_KEY
        )
        self.database = self.client.get_database_client(Config.COSMOS_DB_NAME)
        self.container = self.database.get_container_client(Config.COSMOS_CONTAINER_NAME)
    
    async def store_result(self, transaction_id, event_data, risk_result):
        try:
            document = {
                "id": transaction_id,
                "event_data": event_data,
                "risk_score": risk_result.get("risk_score"),
                "risk_level": risk_result.get("risk_level"),
                "impact": risk_result.get("impact"),
                "recommended_actions": risk_result.get("recommended_actions")
            }
            return await self.container.upsert_item(document)
        except Exception as e:
            logging.error(f"Error storing result in Cosmos DB: {str(e)}")
            raise 