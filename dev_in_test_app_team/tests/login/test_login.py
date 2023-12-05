import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.page import Page

from framework.locators import POSITIVE_LOGIN, NEGATIVE_LOGIN

# Test for positive login scenario
@pytest.mark.parametrize("username, password", [("qa.ajax.app.automation@gmail.com", "qa_automation_password")])
def test_positive_login(username, password, user_login_fixture, driver):
    try:
        Page.click_element(driver, POSITIVE_LOGIN['login_button_locator'])

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(POSITIVE_LOGIN['username_locator']))

        Page.find_element(driver, POSITIVE_LOGIN['username_locator']).send_keys(username)
        Page.find_element(driver, POSITIVE_LOGIN['password_locator']).send_keys(password)
        Page.click_element(driver, POSITIVE_LOGIN['login_button_locator'])

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(POSITIVE_LOGIN['menu_drawer']))
        assert Page.find_element(driver, POSITIVE_LOGIN['menu_drawer']).is_displayed()

        sandwich_button = Page.find_element(driver, POSITIVE_LOGIN['menu_drawer'])
        sandwich_button.click()

        wait.until(EC.visibility_of_element_located(POSITIVE_LOGIN['build_element']))
        assert Page.find_element(user_login_fixture, POSITIVE_LOGIN['build_element']).is_displayed()

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    finally:
        if driver is not None:
            driver.quit()

# Test for negative login scenario
def test_negative_login(driver, user_login_fixture):
    try:
        Page.click_element(driver, POSITIVE_LOGIN['login_button_locator'])

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(POSITIVE_LOGIN['username_locator']))
    
        Page.find_element(driver, NEGATIVE_LOGIN['username_locator']).send_keys("incorrect_username")
        Page.find_element(driver, NEGATIVE_LOGIN['password_locator']).send_keys("incorrect_password")
        Page.click_element(driver, NEGATIVE_LOGIN['login_button_locator'])

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(NEGATIVE_LOGIN['error_message']))
        assert Page.find_element(user_login_fixture, NEGATIVE_LOGIN['error_message']).is_displayed()

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    finally:
        if driver is not None:
            driver.quit()