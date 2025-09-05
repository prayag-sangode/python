import logging

# Configure logging
logging.basicConfig(
    filename="app.log",          # log file name
    filemode="w",                # overwrite on each run
    level=logging.DEBUG,         # log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Different log levels
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

print("Logs have been written to app.log")
