from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)

def test_logger_and_exception(a,b):
    try:
        result = a/b
        logger.info("Testing logger and exception handling")
        return result
    except Exception as e:
        logger.error("An error occurred")
        raise CustomException("Custom erroe message", sys) from e

if __name__ == "__main__":
    try:
        logger.info("Starting the script")
        test_logger_and_exception(5,0)  # This will work fine
    except CustomException as e:
        logger.error(str(e))