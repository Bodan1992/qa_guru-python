# общий файл для текстур на весь проект или модуль распространяются
import pytest
from selene.support.shared import browser
from selenium import webdriver
browser.config.driver = webdriver.Chrome()

@pytest.fixture()
def url():
    browser.open('https://www.ecosia.org/')


@pytest.fixture()
def browser_size():
    browser.driver.set_window_size(1080, 720)