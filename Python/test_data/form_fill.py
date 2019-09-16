from time import sleep

from Python.test_data import driver_container
from Python.test_data.test_form_cv import Form


class TestFillForm:

    def setup(self):
        self.driver = driver_container.driver

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_fill_form(self):
        self.driver.get('https://newsilpo.iir.fozzy.lan/work/info/storinka-ambassadora')

        form = Form()

        form.open_form()
        form.fill_name()
        form.fill_adress()
        form.fill_birthday()
        form.fill_phone()
        form.fill_email()
        form.fill_university()
        form.fill_specialization()
        form.fill_grade()
        form.fill_reason()
        sleep(10)
        assert form.is_submit_btn_active()
