import logging

from status.get import GetStatus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    return GetStatus.get()
