import logging


def passedLog(command: str):
    passedLog = logging.basicConfig(filename='commandsPassedLog.log', level=logging.info,
                                    format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    log_info = logger.info(f"AN INTERNAL COMMAND HAS PASSED THE KERNEL")


def failedLog(command: str):
    failedLog = logging.basicConfig(filename='commandsFailedLogs.log', level=logging.ERROR,
                                    format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    log_info = logger.error(f"A FOREIGN COMMAND HAS BEEN REJECTED BY THE KERNEL")

