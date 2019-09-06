from selenium.webdriver.common.by import By

from Python.db_SQLAlchemy.queries.thread_queries_preconditions import Insert, DeleteFromTable
from Python.threads_part.base_test import BaseTest


class TestExample(BaseTest):
    def __init__(self):
        super(TestExample, self).__init__()

    def setup(self):
        self.driver.get("http://newsilpo.iir.fozzy.lan")

    def preconditions(self):
        DeleteFromTable().del_vacancy_by_manager_name("Nescafe")
        Insert().ins_vacancy()

    def test(self):

        self.driver.get("http://newsilpo.iir.fozzy.lan/work/vacancies")
        vacancies = self.driver.find_element(By.NAME, 'vacancy')
        vacancies.click()
        vacancies_list = self.driver.find_elements(By.CLASS_NAME, 'autocomplete-item')
        for vacancy in vacancies_list:
            if vacancy.text == 'Администратор':
                vacancy.click()
        qtt_of_vacancies = self.driver.find_elements(By.CLASS_NAME, 'vacancies-list-item-wrapper')

        assert qtt_of_vacancies > 0

    def postconditions(self):
        DeleteFromTable().del_vacancy_by_manager_name("Nescafe")

    def teardown(self):
        self.driver.close()
        self.driver.quit()