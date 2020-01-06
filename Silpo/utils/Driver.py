from selenium import webdriver


class Driver:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path='C:\\Work\\Projects\\DK-09-2019\\Silpo'
                                                       '\\utils\\drivers\\chromedriver.exe',
                                       chrome_options=options)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
