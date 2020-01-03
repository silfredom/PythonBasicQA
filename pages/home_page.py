# -*- coding: UTF-8 -*-
from nose.tools import assert_false, assert_equals
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class HomePage(object):
    """Page class for home?"""

    # web elements locators
    we_title = (By.CSS_SELECTOR, ".what-is-cornershop")
    we_login_button = (By.CSS_SELECTOR, ".user-login-button > button")
    we_register_button = (By.CSS_SELECTOR, ".user-register-button > button")

    # text present on the page for assertions but i dont know if i have time for this atm
    text_span = u"We deliver your groceries in one hour"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_modal(self, time):
        """fluent wait until tittle present"""
        wait = WebDriverWait(self.driver, time)
        wait.until(lambda driver: self.driver.find_element(*HomePage.we_title))

    def verify_authenticate_modal(self):
        """verify initial state of the page TODO after funtional part is being done"""
        print("checking statics elements TODO")

    def authenticate_click_button(self):
        """click authenticate button"""
        self.driver.find_element(*HomePage.we_register_button).click()

    def login_click_button(self):
        """click login button"""
        self.driver.find_element(*HomePage.we_login_button).click()