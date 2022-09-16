import logging
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)-12s %(message)s",
    datefmt="%m-%d %H:%M",
    filename="guard-rail.log",
    filemode="w",
)


console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s: %(levelname)-8s - %(message).500s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

LOG = logging.getLogger(__name__)


def logdebug(func: object):
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_msg = func.__name__
        entry_message = f"{log_msg} started"
        LOG.info(entry_message)
        result = func(*args, **kwargs)
        exit_message = f"{log_msg} complete"
        LOG.info(exit_message)
        return result

    return wrapper
