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
        self.driver.get('https://newsilpo.iir.fozzy.lan/work/info/ambasador')

        form = Form()

        form.open_form()
        sleep(1)
        form.fill_name()
        sleep(1)
        form.fill_adress()
        sleep(1)
        form.fill_birthday()
        sleep(1)
        form.fill_phone()
        sleep(1)
        form.fill_email()
        sleep(1)
        form.fill_university()
        sleep(1)
        form.fill_specialization()
        sleep(1)
        form.fill_grade()
        sleep(1)
        form.fill_reason()
        sleep(2)
        assert form.is_submit_btn_active()
