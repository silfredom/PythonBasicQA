# -*- coding: UTF-8 -*-
import time

from behave import *
from pages.home_page import HomePage
from pages.register_page import RegisterPage


@given(u'I navigate to Cornershop')
def step_impl(context):
    driver = context.driver
    driver.get(context.base_url)
    home = HomePage(driver)
    home.wait_for_modal(context.timeout)
    home.verify_authenticate_modal()
    home.authenticate_click_button()


@given(u'I Sign up using this information')
def step_impl(context):
    driver = context.driver
    register = RegisterPage(driver)
    register.verify_signup_form()
    for line in context.table:
        email = line["Email"]
        name = line["Name"]
        last_name = line["Last name"]
        password = line["Password"]
        register.signup(email, name, last_name, password)


@then(u'A message should be present stating: "{text}"')
def step_impl(context, text):
    driver = context.driver
    register = RegisterPage(driver)
    register.checkmsg(text)












