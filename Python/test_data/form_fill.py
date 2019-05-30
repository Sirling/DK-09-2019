from time import sleep

from Python.test_data.driver import Driver
from Python.test_data.test_form_cv import Form

class TestFillForm:

    def setup(self):
        self.driver = Driver().driver

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_fill_form(self):
        self.driver.open('https://newsilpo.iir.fozzy.lan')

        form = Form()
        form.open_form()\
            .fill_name()\
            .fill_adress()\
            .fill_birthday()\
            .fill_phone()\
            .fill_email()\
            .fill_university()\
            .fill_specialization()\
            .fill_grade()\
            .fill_reason()
        sleep(10)
        assert form.is_submit_btn_active()