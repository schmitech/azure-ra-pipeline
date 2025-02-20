from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
from ..config import Config

class Telemetry:
    def __init__(self):
        exporter = AzureMonitorTraceExporter(
            connection_string=Config.APPINSIGHTS_CONNECTION_STRING
        )
        
        trace.set_tracer_provider(TracerProvider())
        span_processor = BatchSpanProcessor(exporter)
        trace.get_tracer_provider().add_span_processor(span_processor)
        
        self.tracer = trace.get_tracer(__name__)
    
    def start_span(self, name):
        """Start a new trace span"""
        return self.tracer.start_as_current_span(name) 