import logging
import json
import sys

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }
        if hasattr(record, "trace_id"):
            log["trace_id"] = record.trace_id
        return json.dumps(log)

def get_logger(name="agent-orchestrator"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
