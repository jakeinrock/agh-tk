import logging

def create_logger(log_name):
    """Creating the customized logger"""
    logging.basicConfig(format='%(asctime)s - %(name)s%(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S%p')
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    return logger
