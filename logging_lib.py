import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from config import Config
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
import os
import uuid
import sys



def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    format_str = '%(asctime)s - %(levelname)-8s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(format_str, date_format)
    handler = AzureLogHandler(connection_string=str(Config.APP_INSIGHTS_CONNECTION_STRING))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()
