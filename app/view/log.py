import logging

FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def set_logger(name, log_file, level):
    handler = logging.FileHandler(log_file)
    handler.setFormatter(FORMATTER)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

LOGGER_ERR = set_logger('Error_logger', 'app/logs/error_msg.log', logging.ERROR)
LOGGER_DEB = set_logger('Debug_logger', 'app/logs/debug_msg.log', logging.ERROR)
LOGGER_AUD = set_logger('Sql_Audit', 'app/logs/sql_audit.log', logging.ERROR)
LOGGER_MSG = set_logger('Sql_Access', 'app/logs/sql_msg.log', logging.ERROR)
LOGGER_ACC = set_logger('Error_logger', 'app/logs/sql_acc.log', logging.ERROR)
logfilepath = r'E:\\web_applications\\RAP-DEV\\Risk-Appetite_Reporting\\app\\logs'

def logger_error():
    return LOGGER_ERR

def logger_debug():
    return LOGGER_DEB

def logger_audit():
    return LOGGER_AUD

def logger_msg():
    return LOGGER_MSG

def logger_acc():
    return LOGGER_ACC

