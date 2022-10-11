import logging

logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

debug_ = logger.debug("A debug message")
info_ = logger.info("An information message")
warning_ = logger.warning("It's a severe warning")
error_ = logger.error("A Hard error has occurred")
critical_ = logger.critical("A critical error has occurred")
