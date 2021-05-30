import inspect
import logging
import os
import random

import pytest

"""PIL is a library that help to get screenshots. Should be install as <pip install pillow>"""
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""импортим данные из установленноей <pip install scikit-image>библиотеки, дабы сравниваь картинки"""
from skimage import io as image_io
from skimage.metrics import structural_similarity

from test_data.base_input_text import TEXT_INPUT_ENG


@pytest.mark.usefixtures("setup")
class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    """создали методы на основании Explicit Wait который можем вызывать дабы проверять отображается ли определенный
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

    def verify_element_images(self, locator_type, locator, expected_image_path):
        """Get screenshot"""
        """crop element"""
        try:
            # будет создан полный скриншот страницы и созранен в screenshot.png
            self.driver.save_screenshot(filename="screenshot.png")
            element = self.wait_until_find(locator_type=locator_type, locator=locator)
            top = element.rect["y"]
            bottom = element.rect["y"] + element.rect["height"]
            left = element.rect["x"]
            right = element.rect["x"] + element.rect["width"]

            """Crop image"""
            # также будет создан обрезанный скриншот с нужным нам элементом
            image_obj = Image.open("screenshot.png")
            cropped_image = image_obj.crop((left, top, right, bottom))
            cropped_image.save("cropped_image.png")

            # compare images
            actual_image = image_io.imread("cropped_image.png")
            expected = image_io.imread(expected_image_path)
            import logging
            """тут логируем насколько % совпадает картинка"""
            logging.critical(structural_similarity(actual_image, expected, multichannel=True))
            """structural_similarity(actual_image, expected, multichannel=True) == 0.9 означает что совпадение должно быть больше чем на 90%"""
            assert structural_similarity(actual_image, expected, multichannel=True) > 0.9
        # если ошибка то получаем данную ошибку
        except Exception as exception:
            raise exception

        # а тут если ошибки таки нету, то удаляем наш скриншот который содержит обрезанный имейдж в ACTUAL RESULT
        else:
            os.remove("cropped_image.png")

        # в любом случае удаляем наш общий скриншот всего экрана
        finally:
            os.remove("screenshot.png")

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


"""создали юзера который принимает и сохранет в себя данные параметры"""


class AdminUser:
    def __init__(self, password, email):
        self.password = password
        self.email = email


def generate_random_text(word_count=3):
    # word_count=3 - это сколько по дефолту будет слов
    """Generate random text based on input text
     - Вначале реплейсим все энтер на пустую строку
     - раскладываем текст на множество с помощью сплита убираем пробелы
     - итого получаем массив слов"""
    input_text_lst = TEXT_INPUT_ENG.replace("\n", "").split(" ")
    generatet_text = []
    generatet_text_lst = []
    for _ in range(word_count):
        generatet_text_lst.append(random.choice(input_text_lst))
        generatet_text = ' '.join(generatet_text_lst)
    return generatet_text
