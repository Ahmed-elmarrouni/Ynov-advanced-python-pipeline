import logging
import sys


def setup_logging():
    logger = logging.getLogger("datapipeline")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    fh = logging.FileHandler("pipeline.log")
    fh.setFormatter(formatter)

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)

    # I added this check so logs don't print twice
    if not logger.handlers:
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
