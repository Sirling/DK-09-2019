from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Python.test_data.driver import Driver
from Python.test_data.screen_listener import ScreenshotListener

driver = Driver().driver
# driver = EventFiringWebDriver(driver_container, ScreenshotListener())
wait = WebDriverWait(driver, 5)

