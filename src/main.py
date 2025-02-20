import asyncio
import logging
from ingestion.event_hub_client import EventHubHandler
from analysis.risk_analyzer import RiskAnalyzer
from monitoring.telemetry import Telemetry

async def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Initialize components
    event_hub = EventHubHandler()
    risk_analyzer = RiskAnalyzer()
    telemetry = Telemetry()
    
    try:
        # Start receiving events
        logging.info("Starting risk assessment pipeline...")
        await event_hub.start_receiving()
    except KeyboardInterrupt:
        logging.info("Shutting down...")
    except Exception as e:
        logging.error(f"Error in main: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 