from abc import ABC, abstractmethod
from selenium.webdriver.support.wait import WebDriverWait
from Silpo.utils.Driver import Driver


class BaseTest(ABC):

    driver = Driver().driver
    wait = WebDriverWait(driver, 5)


    @abstractmethod
    def preconditions(self):
        """
        Абстрактный метод
        Подготовка к тесту
        """
        pass

    @abstractmethod
    def execution_test(self):
        """
        Абстрактный метод
        Выполнение теста
        """
        pass

    @abstractmethod
    def postconditions(self):
        """
        Абстрактный метод
        Зачистка после теста / возврат исходных параметров
        """
        pass
