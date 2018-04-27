# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver


def is_alert_present(wd):
    try:
        var = wd.switch_to_alert().text
        return True
    except:
        return False


class Test_login(unittest.TestCase):

    def setUp(self):
        path_geckodriver = '/Users/mikhail.shchegolev/PycharmProjects/geckodriver'
        host = "https://v4online.atol.ru"
        pageUrl = "/lk/Account/Login?returnUrl=%2Flk%2F"
        self.wd = WebDriver(executable_path=path_geckodriver)
        self.wd.implicitly_wait(60)

    def test_login(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="+79216527446", password="1QAZ!qaz")
        self.logout(wd)

    def logout(self, wd):
        if wd.find_element_by_id('clientName').is_displayed():
            wd.find_element_by_id('clientName').click()
            if wd.find_element_by_xpath("//ul[@class='dropdown-menu']//a[.='Выход']").is_displayed():
                wd.find_element_by_xpath("//ul[@class='dropdown-menu']//a[.='Выход']").click()

    def add_company(self, wd):
        wd.find_element_by_xpath(
            'normalize-space(//span[@class="flat-button-content"]/text()["Добавить компанию"])').click()

    def choose_business_entity_type(self, wd):
        wd.find_element_by_xpath(
            '//div[@class="form-group form-group-sm"]/label[@for="BusinessEntityType"]/..//button').click()

    def login(self, wd, username, password):
        wd.find_element_by_id("Login").click()
        wd.find_element_by_id("Login").clear()
        wd.find_element_by_id("Login").send_keys(username)
        wd.find_element_by_id("Password").click()
        wd.find_element_by_id("Password").clear()
        wd.find_element_by_id("Password").send_keys(password)
        wd.find_element_by_xpath('//input[@value="Вход"]').click()

    def open_home_page(self, wd):
        wd.get("https://v4online.atol.ru/lk/Account/Login?returnUrl=%2Flk%2FCompany%2FList")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    var = unittest.main
