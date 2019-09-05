from Python.threads_part.base_test import BaseTest


class TestExample(BaseTest):
    def __init__(self):
        super(TestExample, self).__init__()

    def setup(self):
        self.driver.driver.get("http://newsilpo.iir.fozzy.lan")

    def preconditions(self):


