from Python.test_data.driver import Driver


class TestFillForm:

    def setup(self):
        self.driver = Driver().driver

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    def test_fill_form(self):
        self.driver.open('https://newsilpo.iir.fozzy.lan')

