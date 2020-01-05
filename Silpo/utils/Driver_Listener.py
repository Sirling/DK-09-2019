from selenium.webdriver.support.events import AbstractEventListener


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):

        screenshot_name = "no_element.png"
        driver.wrapped_driver.get_screenshot_as_file(screenshot_name)
        print("Screenshot saved as {}".format(screenshot_name))

