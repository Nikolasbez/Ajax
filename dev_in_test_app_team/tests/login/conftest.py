import pytest

from framework.page import Page


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield Page(driver)
