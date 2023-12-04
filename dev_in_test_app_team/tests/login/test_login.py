from time import sleep

#def test_user_login(user_login_fixture):
    #assert True

def test_login_successful(driver):
        # Locate login elements and interact with them
        login_button = driver.find_element_by_xpath ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        login_button.click()

        sleep(3)

        # Find the login fields and button
        username_field = driver.find_element_by_xpath('(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')
        password_field = driver.find_element_by_xpath('(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]')

        sleep(3)

        submit_button = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')

        # Login
        username_field.clear()
        password_field.clear()
        username_field.send_keys('qa.ajax.app.automation@gmail.com')
        password_field.send_keys('qa_automation_password')
        submit_button.click()

        # Wait for the login process to complete
        sleep(3)

        # Check if the user is logged in successfully by verifying an element that appears after login
        assert driver.find_element_by_id('com.ajaxsystems:id/menuDrawer').is_displayed()

        sandwich_button = driver.find_element_by_id('com.ajaxsystems:id/menuDrawer')
        sandwich_button.click()

        sleep(3)

        assert driver.find_element_by_id('com.ajaxsystems:id/build').is_displayed()

def test_login_failed(driver):

        # Locate login elements and interact with them
        login_button = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        login_button.click()

        sleep(3)

        # Find the login fields and button
        username_field = driver.find_element_by_xpath('(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')
        password_field = driver.find_element_by_xpath('(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]')

        sleep(3)

        submit_button = driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')

        # Login
        username_field.clear()
        password_field.clear()
        username_field.send_keys('test_login')
        password_field.send_keys('test_password')
        submit_button.click()

        # Wait for the login process to complete
        sleep(3)

        # Check if the error message element is displayed when login fails
        assert driver.find_element_by_id('com.ajaxsystems:id/snackbar_text').is_displayed()
