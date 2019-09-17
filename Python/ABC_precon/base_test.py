from abc import ABC, abstractmethod
from selenium.webdriver.support.wait import WebDriverWait
from Python.test_data.driver_container import driver


class BaseTest(ABC):

    driver = driver
    # кастомный вейт
    wait = WebDriverWait(driver, 5)

    @abstractmethod
    def preconditions(self):
        """
        Абстрактный метод
        Подготовка к тесту
        """
        pass

    @abstractmethod
    def test(self):
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
