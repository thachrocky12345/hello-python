import os


class Config:
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    RABBITMQ_ROUTING_KEY = os.environ.get('ENV2', 'test')
    APP_INSIGHTS_CONNECTION_STRING = os.environ.get('APP_INSIGHTS_CONNECTION_STRING', 'app_insights')
