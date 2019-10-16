from time import sleep

from selenium.webdriver.common.by import By
from Python.test_data.driver_container import driver, wait
from Python.test_data.faker_lib import DataCreatorFake
from selenium.webdriver.support import expected_conditions as EC


class Form:
    data = DataCreatorFake()

    def open_form(self):

        form_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class*="btn-proceed"]')))
        driver.execute_script("return arguments[0].scrollIntoView();", form_button)
        sleep(5)
        form_button.click()
        return self

    def fill_name(self):

        name = driver.find_element(By.CSS_SELECTOR, 'input[name="fullName"]')
        name.clear()
        name.send_keys(self.data.create_name('full'))
        return self

    def fill_adress(self):

        address = driver.find_element(By.CSS_SELECTOR, 'input[name="placeOfResidence"]')
        address.clear()
        address.send_keys(self.data.create_address())
        return self

    def fill_birthday(self):

        date = driver.find_element(By.CSS_SELECTOR, 'input[name="birthday"]')
        date.clear()
        date.send_keys(self.data.create_birth_date())
        return self

    def fill_phone(self):

        phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
        phone.clear()
        phone.send_keys(self.data.create_phone_number())
        return self

    def fill_email(self):

        email = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email.clear()
        email.send_keys(self.data.create_email())
        return self

    def fill_university(self):

        university = driver.find_element(By.CSS_SELECTOR, 'input[name="university"]')
        university.clear()
        university.send_keys("Kiev National University of Construction and Architecture")
        return self

    def fill_specialization(self):

        specialty = driver.find_element(By.CSS_SELECTOR, 'input[name="specialization"]')
        specialty.clear()
        specialty.send_keys("Geoinformational technologies")
        return self

    def fill_grade(self):

        from random import randint
        grade = driver.find_element(By.CSS_SELECTOR, 'input[name="grade"]')
        grade.clear()
        grade.send_keys(randint(1, 9))
        return self

    def fill_reason(self):

        reason = driver.find_element(By.CSS_SELECTOR, 'textarea[name="ambasadorParticipation"]')
        driver.execute_script("return arguments[0].scrollIntoView();", reason)
        reason.clear()
        reason.send_keys(self.data.create_text(500))
        return self

    def is_submit_btn_active(self):

        try:
            button = driver.find_element(By.CSS_SELECTOR, 'button[class*="ambasador-form__btn-submit"]')
            driver.execute_script("return arguments[0].scrollIntoView();", button)
        except Exception as ex:
            raise ex
        if button.is_enabled():
            return True
        elif not button.is_enabled():
            return False
