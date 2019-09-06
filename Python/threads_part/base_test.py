from abc import ABC, abstractmethod
from Python.test_data.driver import Driver


class BaseTest(ABC):

    def __init__(self):
        self.driver = Driver().driver

    @abstractmethod
    def preconditions(self):
        """
        Preparation for test
        """
        pass

    @abstractmethod
    def test(self):
        """
        Test execution
        """
        pass

    @abstractmethod
    def postconditions(self):
        """
        Cleanup after test
        """
        pass
