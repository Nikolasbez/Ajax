from .locators import POSITIVE_LOGIN, NEGATIVE_LOGIN

class Page:

    def __init__(self, driver):
        self.driver = driver

# Function to find an element using locator key from POSITIVE_LOGIN or NEGATIVE_LOGIN
    def find_element(driver, locator_key):
        if locator_key in POSITIVE_LOGIN:
            locator = POSITIVE_LOGIN[locator_key]
        elif locator_key in NEGATIVE_LOGIN:
            locator = NEGATIVE_LOGIN[locator_key]
        else:
            raise KeyError(f"Locator key '{locator_key}' not found")
    
        return driver.find_element(*locator)

# Function to click on an element using locator key from POSITIVE_LOGIN or NEGATIVE_LOGIN
    def click_element(driver, locator_key):
        element = driver.find_element(driver, locator_key)
        element.click()

# Function to locate the element representing a successful login
    def find_menu_drawer(driver):
        return driver.find_element(*POSITIVE_LOGIN['menu_drawer'])

# Function to locate the build element visible after successful login
    def find_build_element(driver):
        return driver.find_element(*POSITIVE_LOGIN['build_element'])

# Function to locate the error message element after a failed login attempt
    def find_error_message(driver):
        return driver.find_element(*NEGATIVE_LOGIN['error_message'])

    
