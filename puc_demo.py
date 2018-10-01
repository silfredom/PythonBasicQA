# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time

class UntitledTestCase(unittest.TestCase):

    def setUp(self):

        path = "/usr/local/bin/chromedriver"
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://demo.phpmyadmin.net/master-config/")
        driver.find_element_by_xpath("//ul[@id='topmenu']/li[4]/a").click()
        driver.find_element_by_id("add_user_anchor").click()
        driver.find_element_by_id("pma_username").send_keys("santiago")
        driver.find_element_by_id("text_pma_pw").send_keys("PUCcurso123")
        driver.find_element_by_id("text_pma_pw2").send_keys("PUCcurso123")
        indicador = driver.find_element_by_id("password_strength")
        label = indicador.text
        assert label == "Strong"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


#########
#python puc_demo.py


