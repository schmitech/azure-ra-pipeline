from langchain.chat_models import AzureChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from ..config import Config
import logging

class RiskAnalyzer:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            openai_api_key=Config.OPENAI_API_KEY,
            openai_api_version="2023-05-15",
            azure_endpoint=Config.OPENAI_ENDPOINT,
            deployment_name=Config.OPENAI_DEPLOYMENT_NAME
        )
        
        self.prompt = ChatPromptTemplate.from_template("""
            Analyze this transaction for potential risks:
            {event_data}
            
            Consider the following factors:
            1. Transaction amount and frequency patterns
            2. User history and behavior
            3. Geographic location and time
            4. Transaction type and category
            
            Provide a detailed risk assessment in JSON format with the following structure:
            {
                "risk_score": <0-100>,
                "risk_level": "<Low/Medium/High>",
                "impact": "<description of potential impact>",
                "recommended_actions": [<list of specific actions>],
                "reason": "<detailed explanation>"
            }
        """)
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    async def analyze_risk(self, event_data):
        """Analyze risk from event data"""
        try:
            result = await self.chain.arun(event_data=event_data)
            return result
        except Exception as e:
            logging.error(f"Error analyzing risk: {str(e)}")
            return None 