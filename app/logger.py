from elasticsearch import Elasticsearch
import logging
import os

es = Elasticsearch([os.getenv("ELASTICSEARCH_URL")])

class ElasticsearchHandler(logging.Handler):
    def __init__(self, es_client, index_name):
        super().__init__()
        self.es_client = es_client
        self.index_name = index_name

    def emit(self, record):
        log_entry = self.format(record)
        self.es_client.index(index=self.index_name, body={'message': log_entry})

logger = logging.getLogger('email_service')
logger.setLevel(logging.INFO)
es_handler = ElasticsearchHandler(es, 'logs')
es_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(es_handler)
