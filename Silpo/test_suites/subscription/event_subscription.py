from Silpo.tests.subscription_phone import ExistingPhone


class TestSubscription(ExistingPhone):

    def setup(self):
        pass

    def test_subcsr(self):
        self.preconditions()
        self.execution_test()
        self.postconditions()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
