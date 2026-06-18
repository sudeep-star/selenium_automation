import logging
import os

class LogGenerator:
    @staticmethod
    def get_logger():

        os.makedirs("logs",exist_ok=True)

        logger=logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler=logging.FileHandler("logs/automation.log")
            formatter= logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(
                formatter
            )
            logger.addHandler(file_handler)
        
        return logger