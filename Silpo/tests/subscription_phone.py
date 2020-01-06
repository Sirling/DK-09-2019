from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Silpo.src.back.DB.queries.Delete_queries.delete_by_phone import delete_phone
from Silpo.src.back.DB.queries.Insert_queries.insert_phone import insert_phone
from Silpo.test_suites.BaseTest import BaseTest


class ExistingPhone(BaseTest):
    event_to_find = 'Beermaster Day 2022 Beermaster'
    phone_to_enter = '0930768886'

    def preconditions(self):
        """
        Прекондишен для теста
        """
        # Удаление записи
        delete_phone(self.event_to_find, self.phone_to_enter)
        # Создание новой записи
        insert_phone(39, self.phone_to_enter)

    def execution_test(self):
        """
        Проверка отображения на сайте созданной ранее вакансии
        """
        # Открытие страницы событий
        self.driver.get("http://newsilpo.iir.fozzy.lan/about/events")
        # Поиск всех тайтлов событий
        events = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[class=list-item__title]')))
        # Поиск нужной вакансии и клик по ней
        for item in events:
            if item.text.lower() == self.event_to_find.lower():
                item.click()
                break
        # Поиск кнопки "Нагадати" и клик по ней
        remind_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                     'button[class*=subscribe__btn]')))
        remind_btn.click()
        # Поиск поля ввода телефона и ввод номера в него
        phone_input_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            'input[name=phone]')))
        phone_input_field.send_keys(self.phone_to_enter)
        subscribe_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        'button[class*=btn-submit]')))
        subscribe_btn.click()
        response_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                           'div[class=error-modal__content]')))

        assert 'Ви вже підписані на дану подію.' in response_message.text, "Текст уведомления не соответствует"

    def postconditions(self):
        """
        Реализованый посткондишен
        """
        # Удаление записи
        delete_phone(self.event_to_find, self.phone_to_enter)
