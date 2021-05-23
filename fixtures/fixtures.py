import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_as_admin(self):
    login_page_obj = LoginPage(self.driver)
    login_page_obj.login_as_admin()
    self.logger.info("user is logged is as admin")