import logging


def pytest_runtest_setup(item):
    """prepare test"""
    log = logging.getLogger(item.name)
    item.cls.logger = log


class BaseTest:
    """BaseTest class for inheritance.Implements test class default variables"""
    logger = logging.getLogger(__name__)