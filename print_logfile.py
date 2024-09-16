import logging
import time
import random
from log_utils import MakeFileHandler

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)

file_handler = MakeFileHandler(filename="log/rotate.log", maxBytes=1024 * 1024, backupCount=3, encoding='utf-8')
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)


def raise_exception_method():
    try:
        1 / 0
    except Exception as e:
        raise ValueError("zero can't be divided") from e


def log():
    logger.debug('This message should go to the log file')
    logger.debug('This message should go to \n the log file')
    logger.info('So should this')
    logger.info('So \n should \n this')
    logger.warning('And this, too')
    logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
    try:
        raise_exception_method()
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    while True:
        interval_time_seconds = random.Random().randint(1, 5)
        time.sleep(interval_time_seconds)
        log()
