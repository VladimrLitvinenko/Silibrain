import inspect
import logging
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseTest:
    """создали метод на основании Explicit Wait который можем вызывать дабы проверять отображается ли определенный
    текст """
    logger = logging.getLogger(__name__)

    def wait_for_text(self, locator_type, locator, text):
        """Wait until text appears in element"""
        self.wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

    def wait_until_find(self, locator_type, locator):
        """Wait until element can be find"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def wait_until_send_keys(self, locator_type, locator, data):
        """Wait until field enabled and send keys"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        field = self.driver.find_element(by=locator_type, value=locator)
        field.clear()
        field.send_keys(data)

    def wait_until_click(self, locator_type, locator):
        """Wait until button clickable and click"""
        self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        self.driver.find_element(by=locator_type, value=locator).click()

    # """BaseTest class for inheritance.Implements test class default variables"""
    # def getLogger(self):
    #     """Как-то этот метод делает так что в лог файле теперь будет содержаться имя тест кейса"""
    #     loggerName = inspect.stack()[1][3]
    #
    #     """создаем объект логгера"""
    #     """__name__ указываем дабы имя наего файла попал в инпуте логгера.
    #      Но потом вместо нейма мы указали loggerName чтоб в лог файле отображалсь имена нужных нам тест кейсов"""
    #     logger = logging.getLogger(loggerName)
    #
    #     """
    #     - asctime - это переменная которая сожержит время
    #     - levelname - показывает тип еррора
    #     - name - имя тесткейса
    #     - message - наш месендж который мы заинпутили в логгере
    #     """
    #     fileHandler = logging.FileHandler('logfile.log')
    #
    #     """
    #     Мы должны передать fileHandler'у инфу о нашем форматиге. Поэтому кидаем наш тип форматинга в объект
    #     """
    #     formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #
    #     """
    #     теперь мы коннектим между собой тип форматинга(formatter) и fileHandler с помощью setFormatter метода
    #     """
    #     fileHandler.setFormatter(formatter)
    #
    #     logger.addHandler(fileHandler)
    #
    #     """
    #     here we set the level of our tests
    #     - Debug - all logs will be displaed"""
    #     logger.setLevel(logging.INFO)
    #
    #     logger.debug("A debug statement is executed")
    #     logger.info("Information statement")
    #
    #     """
    #     Warning можно использовать, если мы не хотим фейлить наш тест, а хотим только показать что не то.
    #     К примеру негативный баланс по карте который у нас образовался
    #     """
    #     logging.warning("Something  went wrong")
    #     logging.error("Test case failed")
    #     logger.critical("Critical issue")
    #     return logger


"""создали юзера который принимает и сохранет в себя данные параметры"""

class AdminUser:
    def __init__(self, password, email):
        self.password = password
        self.email = email
