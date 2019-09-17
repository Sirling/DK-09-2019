from selenium.webdriver.support.wait import WebDriverWait

from Python.test_data.driver import Driver

driver = Driver().driver
wait = WebDriverWait(driver, 5)
