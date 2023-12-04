def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'UiAutomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '12',
        'resetKeyboard': True,
        'systemPort': 5037,
        'takesScreenshot': True,
        'udid': '93TAY0FQSU',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
