from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from Python.test_data.driver import Driver
from Python.test_data.screnn_listener import ScreenshotListener

driver = EventFiringWebDriver(Driver().driver, ScreenshotListener())
wait = WebDriverWait(driver, 5)
