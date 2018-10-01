# -*- coding: UTF-8 -*-
import time



@given(u'I navigate to phpmyadmin')
def step_impl(context):
    """abro la pagina"""
    context.driver.get("https://demo.phpmyadmin.net/master-config/")



@given(u'I access to users accounts')
def step_impl(context):

    context.driver.find_element_by_xpath("//ul[@id='topmenu']/li[4]/a").click()
    time.sleep(5)
    context.driver.find_element_by_id("add_user_anchor").click()
    time.sleep(5)


@then(u'I fill the passwords inputs with "{password}"')
def step_impl(context, password):

    context.driver.find_element_by_id("pma_username").send_keys("santiago")
    context.driver.find_element_by_id("text_pma_pw").send_keys(password)
    context.driver.find_element_by_id("text_pma_pw2").send_keys(password)


@then(u'I verify the label is "{label}"')
def step_impl(context, label):
    indicador = context.driver.find_element_by_id("password_strength")
    print(">>>>>>>>>>>>>>>>>>>")
    print(indicador.text)
    print(">>>>>>>>>>>>>>>>>>>")
    assert label == indicador.text













