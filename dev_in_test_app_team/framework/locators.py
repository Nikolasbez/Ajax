from appium.webdriver.common.mobileby import MobileBy

# Locators for positive login scenario
POSITIVE_LOGIN = {
    'username_locator': (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'),
    'password_locator': (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'),
    'login_button_locator': (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]'),
    'menu_drawer': (MobileBy.ID, 'com.ajaxsystems:id/menuDrawer'),
    'build_element': (MobileBy.ID, 'com.ajaxsystems:id/build')
}

# Locator for negative login scenario
NEGATIVE_LOGIN = {
    'username_locator': (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'),
    'password_locator': (MobileBy.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]'),
    'login_button_locator': (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]'),
    'error_message': (MobileBy.ID, 'com.ajaxsystems:id/snackbar_text')
}