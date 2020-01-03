# -*- coding: UTF-8 -*-
from nose.tools import assert_false, assert_equals
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import time


class RegisterPage(object):
    """Page class for register page"""

    # web elements locators
    we_title = (By.CSS_SELECTOR, "header")
    we_email_input = (By.NAME, "username")
    we_name_input = (By.NAME, "first_name")
    we_lastname_input = (By.NAME, "last_name")
    we_password_input = (By.NAME, "password")
    we_register_button = (By.XPATH, "//form[@id='register']/input[6]")
    we_confirmation = (By.CSS_SELECTOR, "p")

    # text present on the page for assertions but i dont know if i have time for this atm
    # text_span = u"We deliver your groceries in one hour"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_title(self, time):
        """fluent wait until tittle present"""
        wait = WebDriverWait(self.driver, time)
        wait.until(lambda driver: self.driver.find_element(*RegisterPage.we_title))

    def verify_signup_form(self):
        """verify initial state of the page TODO after funtional part is being done"""
        print("checking statics elements TODO")

    def signup (self, email, name, last_name, password):
        """sing up using a set of values"""
        if email == "new valid email":
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime("%d%b%Y%H%M%S")
            email = "automationemail"+timestampStr+"@gmail.com"
        self.driver.find_element(*RegisterPage.we_email_input).send_keys(email)
        self.driver.find_element(*RegisterPage.we_name_input).send_keys(name)
        self.driver.find_element(*RegisterPage.we_lastname_input).send_keys(last_name)
        self.driver.find_element(*RegisterPage.we_password_input).send_keys(password)
        self.driver.find_element(*RegisterPage.we_register_button).click()

    def checkmsg(self, text):
        """check confirmation msg"""
        assert_equals(text, self.driver.find_element(*RegisterPage.we_confirmation).text)



