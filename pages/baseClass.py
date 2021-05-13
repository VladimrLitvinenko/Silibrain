import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:
    """BaseTest class for inheritance.Implements test class default variables"""
    logger = logging.getLogger(__name__)