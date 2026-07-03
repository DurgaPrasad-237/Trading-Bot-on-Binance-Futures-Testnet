import logging
import os


def get_logger():
    """
    Returns a configured logger.
    """

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs if get_logger() is called multiple times
    if not logger.handlers:

        file_handler = logging.FileHandler("logs/trading.log")

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger