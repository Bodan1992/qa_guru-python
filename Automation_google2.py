from selene.support.shared import browser
from selene import be, have

from selenium import webdriver

import pytest

browser.config.driver = webdriver.Chrome()

def test_search_valid(browser_size):
    browser.element('[name="q"]').should(be.blank).type('Selene - Web UI browser in Python').press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(have.text("Selene - User-oriented Web UI browser tests in Python"))




#
# def test_search_invalid(windows_size_chrome):
#     browser.open('https://www.ecosia.org/')
#     browser.element('[name="q"]').should(be.blank).type('SeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSadasdsad5q4w4qww4eSeSeSeSeSeSeSeSeSev').press_enter()
#     browser.element('[data-test-id="message-tips-message"]').should(have.text("Yikes! We didn't find any results for “SeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSeSadasdsad5q4w4qww4eSeSeSeSeSeSeSeSeSev”"))
