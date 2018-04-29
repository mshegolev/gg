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
        self.add_company(wd)
        self.choose_business_entity_type(wd, "Индивидуальный предприниматель")
        self.input_inn(wd, "111111111111")
        self.input_ogrn(wd, "012345678912345")
        self.input_email(wd, "atolonline0@gmail.com")
        self.input_phone(wd, "+71234567788")
        self.logout(wd)

    def logout(self, wd):
        if wd.find_element_by_id('clientName').is_displayed():
            wd.find_element_by_id('clientName').click()
            if wd.find_element_by_xpath("//ul[@class='dropdown-menu']//a[.='Выход']").is_displayed():
                wd.find_element_by_xpath("//ul[@class='dropdown-menu']//a[.='Выход']").click()

    def add_company(self, wd):
        wd.find_element_by_xpath("//span[@class=\"flat-button-content\"]/text()[\"Добавить компанию\"]/..").click()

    def choose_business_entity_type(self, wd, business_entity):
        wd.find_element_by_xpath(
            '//div[@class="form-group form-group-sm"]/label[@for="BusinessEntityType"]/..//button').click()
        # todo: add checking
        wd.find_element_by_xpath(
            '//div[@class="col-sm-6"]//ul[@class="multiselect-container dropdown-menu"]'
            '//label[@class="radio" and @title="' + business_entity + '"]').click()

    def input_inn(self, wd, inn):
        wd.find_element_by_id("INN-2").click()
        wd.find_element_by_id("INN-2").clear()
        wd.find_element_by_id("INN-2").send_keys(inn)

    def input_ogrn(self, wd, ogrn):
        wd.find_element_by_id("OGRN-2").click()
        wd.find_element_by_id("OGRN-2").clear()
        wd.find_element_by_id("OGRN-2").send_keys(ogrn)

    def input_phone(self, wd, phone):
        wd.find_element_by_id("Phone").click()
        wd.find_element_by_id("Phone").clear()
        wd.find_element_by_id("Phone").send_keys(phone)

    def input_email(self, wd, email):
        wd.find_element_by_id("EMail").click()
        wd.find_element_by_id("EMail").clear()
        wd.find_element_by_id("EMail").send_keys(email)

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
