from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Python.ABC_precon.thread_queries_preconditions import del_vacancy_by_name, ins_vacancy
from Python.ABC_precon.base_test import BaseTest


class TestExample(BaseTest):

    def preconditions(self):
        """
        Прекондишен для теста
        """
        # Удаление вакансии, если она такая уже существует
        del_vacancy_by_name("Тестовая вакансия")
        # Создание новой вакансии
        ins_vacancy()

    def setup(self):
        # Запуск прекондишенов (необходима их реализация)
        self.preconditions()
        # Запуск драйвера, для ускорения отработки
        self.driver.get("http://newsilpo.iir.fozzy.lan")

    def test(self):
        """
        Проверка отображения на сайте созданной ранее вакансии
        """
        # Открытие страницы вакансий
        self.driver.get("http://newsilpo.iir.fozzy.lan/work/vacancies")
        # Раскрытие автокомплита "Вакансія" и клик по нему
        vacancies = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="vacancy"]')))
        vacancies.click()
        # Поиск всех элементов
        vacancies_list = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'autocomplete-item')))
        # Поиск нужного элемента и клик по нему
        for vacancy in vacancies_list:
            if vacancy.text == 'Администратор':
                vacancy.click()
                break
        # Подсет количества отображенных вакансий
        qtt_of_vacancies = len(self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'vacancies-list-item-wrapper'))))
        print(qtt_of_vacancies)
        assert qtt_of_vacancies > 0, "Список вакансий пуст"

    def postconditions(self):
        # Удаление вакансии
        del_vacancy_by_name("Jacobs")

    def teardown(self):
        # Удаление вакансии и закрытие драйвера
        self.postconditions()
        self.driver.close()
        self.driver.quit()
