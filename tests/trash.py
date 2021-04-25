import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="/home/ihor/PycharmProjects/pythonQALightSelenium/drivers/chromedriver")
driver.maximize_window()
driver.get("https://stg-hospitalprivadopeten.geniusee.space/")
assert "spfggfgace" in driver.current_url