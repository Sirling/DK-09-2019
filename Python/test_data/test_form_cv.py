from random import random
from selenium.webdriver.common.by import By
from Python.test_data import driver_container
from Python.test_data.faker_lib import DataCreatorFake


class Form:

    driver = driver_container.driver
    data = DataCreatorFake()

    def open_form(self):

        form_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class*="btn-proceed"]')
        self.driver.execute_script("return arguments[0].scrollIntoView();", form_button)
        form_button.click()
        return self

    def fill_name(self):

        name = self.driver.find_element(By.CSS_SELECTOR, 'input[name="fullName"]')
        name.clear()
        name.send_keys(self.data.create_name('full'))
        return self

    def fill_adress(self):

        address = self.driver.find_element(By.CSS_SELECTOR, 'input[name="placeOfResidence"]')
        address.clear()
        address.send_keys(self.data.create_address())
        return self

    def fill_birthday(self):

        date = self.driver.find_element(By.CSS_SELECTOR, 'input[name="birthday"]')
        date.clear()
        date.send_keys(self.data.create_birth_date())
        return self

    def fill_phone(self):

        phone = self.driver.find_element(By.CSS_SELECTOR, 'input[name="birthday"]')
        phone.clear()
        phone.send_keys(self.data.create_phone_number())
        return self

    def fill_email(self):

        email = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email.clear()
        email.send_keys(self.data.create_email())
        return self

    def fill_university(self):

        university = self.driver.find_element(By.CSS_SELECTOR, 'input[name="university"]')
        university.clear()
        university.send_keys("Kiev National University of Construction and Architecture")
        return self

    def fill_specialization(self):

        specialty = self.driver.find_element(By.CSS_SELECTOR, 'input[name="specialization"]')
        specialty.clear()
        specialty.send_keys("Geoinformational technologies")
        return self

    def fill_grade(self):

        grade = self.driver.find_element(By.CSS_SELECTOR, 'input[name="grade"]')
        grade.clear()
        grade.send_keys(random(1, 9))
        return self

    def fill_reason(self):

        reason = self.driver.find_element(By.CSS_SELECTOR, 'input[name="ambasadorParticipation"]')
        reason.clear()
        reason.send_keys(self.data.create_text(500))
        return self

    def is_submit_btn_active(self):

        try:
            button = self.driver.find_element(By.CSS_SELECTOR, 'button[class*="ambasador-form__btn-submit"] span')
            self.driver.execute_script("return arguments[0].scrollIntoView();", button)
        except Exception as ex:
           raise ex
        if button.is_enabled():
            return True
        elif not button.is_enabled():
            return False
