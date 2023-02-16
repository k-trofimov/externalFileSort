import logging
import os

import psutil


def process_memory():
    """
    Inner psutil function
    :return: memory usage in mb
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1048576)


def profile(func):
    """
    Decorator function to profile memory usage
    :param func:
    :return: decorated function
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        mem_after = process_memory()
        logging.info(f"{func.__name__}:consumed memory: {mem_after}mb")

        return result

    return wrapper
