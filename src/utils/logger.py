import logging

# Create logger
logger = logging.getLogger("AgentMark0")
logger.setLevel(logging.DEBUG)  # Change to DEBUG for more detailed logs

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler("agent_mark0.log")  # Log file location
file_handler.setLevel(logging.DEBUG)

# Set log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)