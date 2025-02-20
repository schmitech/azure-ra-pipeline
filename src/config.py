import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    EVENTHUB_CONNECTION_STRING = os.getenv("AZURE_EVENTHUB_CONNECTION_STRING")
    OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
    OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    APPINSIGHTS_CONNECTION_STRING = os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING")
    COSMOS_ENDPOINT = os.getenv("AZURE_COSMOS_ENDPOINT")
    COSMOS_KEY = os.getenv("AZURE_COSMOS_KEY")
    COSMOS_DB_NAME = os.getenv("AZURE_COSMOS_DB_NAME", "RiskDB")
    COSMOS_CONTAINER_NAME = os.getenv("AZURE_COSMOS_CONTAINER_NAME", "RiskResults") 