# logger
import logging

class Logger:
    _instance = None
 
    def __new__(cls):
        if cls._instance is None:
            logger = logging.getLogger(__name__)
            logger.setLevel(logging.INFO)

            console_handler = logging.StreamHandler()

            logger.addHandler(console_handler)

            cls._instance = logger
        return cls._instance
