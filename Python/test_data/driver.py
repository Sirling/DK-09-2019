from selenium import webdriver

class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe', chrome_options=options)
        self.driver.get('about:blank')

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
