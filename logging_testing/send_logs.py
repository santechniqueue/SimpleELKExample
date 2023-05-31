import logging

from logging_testing.handlers import ModifiedTCPLogstashHandler

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)
simple_formatter = logging.Formatter(
    '{"level":"%(levelname)s","message":"%(message)s"}'
)
handler = ModifiedTCPLogstashHandler(
    host='localhost',
    port=5000,
    message_type='log_example',
    tags=['example'],
    fqdn=False,
    version=1,
)
handler.setFormatter(simple_formatter)
logger.addHandler(handler)


if __name__ == '__main__':
    logger.info('This is INFO log')
    print('INFO sent')
    logger.warning('This is WARNING log')
    print('WARNING sent')
    logger.error('This is ERROR log')
    print('ERROR sent')
