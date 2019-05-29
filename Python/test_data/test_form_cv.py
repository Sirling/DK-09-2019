from selenium.webdriver.common.by import By
from Python.test_data.faker_lib import DataCreatorFake
from Python.test_data.driver import Driver


class Form:

    driver = Driver().driver
    data = DataCreatorFake()

    def open_form(self):

        self.driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-proceed"]')

    def fill_name(self):

        name =  self.driver.find_element(By.CSS_SELECTOR, 'input=[name="fullName"]')
        name.clear()
        name.send_keys(self.data.create_name('full'))

    def fill_adress(self):

        address = self.driver.find_element(By.CSS_SELECTOR, 'input=[name="placeOfResidence"]')
        address.clear()
        address.send_keys(self.data.create_address())

    def fill_birthday(self):

        date = self.driver.find_element(By.CSS_SELECTOR, 'input=[name="birthday"]')
        date.clear()
        date.send_keys(self.data.create_birth_date())


    def fill_phone(self):

        phone = self.driver.find_element(By.CSS_SELECTOR, 'input=[name="birthday"]')
        phone.clear()
        phone.send_keys(self.data.create_phone_number())