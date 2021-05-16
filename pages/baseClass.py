import inspect
import logging

import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:
    """BaseTest class for inheritance.Implements test class default variables"""
    def getLogger(self):
        """Как-то этот метод делает так что в лог файле теперь будет содержаться имя тест кейса"""
        loggerName = inspect.stack()[1][3]

        """создаем объект логгера"""
        """__name__ указываем дабы имя наего файла попал в инпуте логгера.
         Но потом вместо нейма мы указали loggerName чтоб в лог файле отображалсь имена нужных нам тест кейсов"""
        logger = logging.getLogger(loggerName)

        """
        - asctime - это переменная которая сожержит время
        - levelname - показывает тип еррора
        - name - имя тесткейса
        - message - наш месендж который мы заинпутили в логгере
        """
        fileHandler = logging.FileHandler('logfile.log')

        """
        Мы должны передать fileHandler'у инфу о нашем форматиге. Поэтому кидаем наш тип форматинга в объект
        """
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        """
        теперь мы коннектим между собой тип форматинга(formatter) и fileHandler с помощью setFormatter метода
        """
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        """
        here we set the level of our tests
        - Debug - all logs will be displaed"""
        logger.setLevel(logging.INFO)

        logger.debug("A debug statement is executed")
        logger.info("Information statement")

        """
        Warning можно использовать, если мы не хотим фейлить наш тест, а хотим только показать что не то.
        К примеру негативный баланс по карте который у нас образовался
        """
        logging.warning("Something  went wrong")
        logging.error("Test case failed")
        logger.critical("Critical issue")
        return logger