import logging
import os
from fluent import handler as fluent_handler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('app')

fluent_host = os.getenv("FLUENTD_HOST", "localhost")
fluent_port = int(os.getenv("FLUENTD_PORT", 24224))
fluent_tag = os.getenv("FLUENTD_TAG", "app")

fluentd_handler = fluent_handler.FluentHandler(fluent_tag, host=fluent_host, port=fluent_port)
formatter = fluent_handler.FluentRecordFormatter({
    'host': '%(hostname)s',
    'where': '%(module)s.%(funcName)s',
    'type': '%(levelname)s',
    'stack_trace': '%(exc_text)s',
})
fluentd_handler.setFormatter(formatter)

logger.addHandler(fluentd_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)
