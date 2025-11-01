import logging
import json
from datetime import datetime
import sys

LOG_FILE = "debate_log.txt"

def setup_logger():
    logger = logging.getLogger("debate")
    logger.setLevel(logging.DEBUG)
    if logger.handlers:
        return logger

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    fh = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    return logger

logger = setup_logger()

def log_state(event: str, payload):
    """
    Log structured state payload (will be JSON-serializable).
    """
    try:
        payload_str = json.dumps(payload, ensure_ascii=False)
    except Exception:
        payload_str = str(payload)
    logger.info(f"STATE | {event} | {payload_str}")

def log_msg(role: str, text: str):
    """
    Log a chat/message line.
    """
    logger.info(f"MSG | {role} | {text}")
