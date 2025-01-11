import logging

def setup_logging():
    logging.basicConfig(
        filename="trading_bot_log.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            # Unpack args and kwargs properly
            return func(*args, **kwargs)
        except TypeError as e:
            logging.error(f"Error in {func.__name__}: {e}")
            if "unexpected keyword argument" in str(e):
                logging.error(f"Unexpected keyword arguments: {kwargs}")
            raise e
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {e}", exc_info=True)
            return f"Error in {func.__name__}: {str(e)}"
    return wrapper
