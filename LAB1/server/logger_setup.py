

import logging
import os


def ensure_log_directories():
   
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    logs_dir = os.path.join(base_dir, "logs")

    os.makedirs(logs_dir, exist_ok=True)

    return logs_dir


def setup_server_logger():
    
    logs_dir = ensure_log_directories()
    log_file = os.path.join(logs_dir, "server.log")

    logger = logging.getLogger("chat_server")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


def setup_gdpr_logger():
    
    logs_dir = ensure_log_directories()
    log_file = os.path.join(logs_dir, "gdpr_violations.log")

    logger = logging.getLogger("gdpr_logger")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger