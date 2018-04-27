# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

success = True
wd = WebDriver()
wd.implicitly_wait(60)


def is_alert_present(wd):
    try:
        var = wd.switch_to_alert().text
        return True
    except:
        return False


try:
    wd.get("https://v4online.atol.ru/lk/Account/Login?returnUrl=%2Flk%2FCompany%2FList")
    wd.find_element_by_id("Login").click()
    wd.find_element_by_id("Login").clear()
    wd.find_element_by_id("Login").send_keys("+79216527446")
    wd.find_element_by_id("Password").click()
    wd.find_element_by_id("Password").clear()
    wd.find_element_by_id("Password").send_keys("1QAZ!qaz")
    wd.find_element_by_xpath("//div[1]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/input").click()
    wd.find_element_by_xpath("//div[1]/div[2]/div[2]/div/div/div/div[2]/form/div[3]/div/div/input").send_keys("")
    wd.find_element_by_xpath("//div[@class='row']/div").click()
    wd.find_element_by_xpath("//div[@class='col-md-7']/div[1]/div[2]/div/div/div/button").click()
    wd.find_element_by_link_text("Юридическое лицо").click()
    wd.find_element_by_xpath("//div[@class='col-md-7']/div[1]/div[2]/div/div/div/ul/li[1]/a/label/input").click()
    wd.find_element_by_id("BusinessEntitySubTypeName").click()
    wd.find_element_by_id("BusinessEntitySubTypeName").clear()
    wd.find_element_by_id("BusinessEntitySubTypeName").send_keys("ооо")
    wd.find_element_by_id("Name").click()
    wd.find_element_by_id("Name").clear()
    wd.find_element_by_id("Name").send_keys("ооо морковка")
    wd.find_element_by_id("INN-1").click()
    wd.find_element_by_id("INN-1").clear()
    wd.find_element_by_id("INN-1").send_keys("1111111111")
    wd.find_element_by_id("OGRN-1").click()
    wd.find_element_by_id("OGRN-1").clear()
    wd.find_element_by_id("OGRN-1").send_keys("2222222222222")
    wd.find_element_by_id("KPP").click()
    wd.find_element_by_id("KPP").clear()
    wd.find_element_by_id("KPP").send_keys("333333333")
    wd.find_element_by_id("addrEdit").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/button").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/div/div[1]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/div/div[1]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/div/div[1]/input").send_keys("мос")
    wd.find_element_by_link_text("г. Москва").click()
    if not wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/select//option[2]").is_selected():
        wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[1]/div/select//option[2]").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[4]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[4]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[4]/input").send_keys("111111")
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/button").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/div/div[1]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/div/div[1]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/div/div[1]/input").send_keys("1")
    wd.find_element_by_link_text("ул. 10-летия Октября").click()
    if not wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/select//option[2]").is_selected():
        wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[3]/div/select//option[2]").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[6]/input").click()
    wd.find_element_by_link_text("11").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[7]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[7]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[7]/input").send_keys("1")
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[9]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[9]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[9]/input").send_keys("1")
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[10]/input").click()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[10]/input").clear()
    wd.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div[10]/input").send_keys("1")
    wd.find_element_by_xpath("//div[5]/div/div/div[3]/button[1]").click()
    wd.find_element_by_xpath("//div[@class='col-md-7']/div[4]").click()
    wd.find_element_by_id("Phone").click()
    wd.find_element_by_id("Phone").clear()
    wd.find_element_by_id("Phone").send_keys("+71111111111")
    wd.find_element_by_id("EMail").click()
    wd.find_element_by_id("EMail").clear()
    wd.find_element_by_id("EMail").send_keys()
    wd.find_element_by_id("EMail").click()
    wd.find_element_by_id("EMail").clear()
    wd.find_element_by_id("EMail").send_keys("atolgg@gmail.ru")
    if not wd.find_element_by_id("IsAcceptedOffer").is_selected():
        wd.find_element_by_id("IsAcceptedOffer").click()
    wd.switch_to_frame()
    wd.find_element_by_xpath("//div[1]/p[7]").click()
    wd.switch_to_default_content()
    wd.find_element_by_xpath("//div[6]/div/div/div[3]/button").click()
    wd.find_element_by_id("nextButton").click()
    wd.find_element_by_xpath("//div[@class='col-md-7']//button[.='Не выбрано']").click()
    if not wd.find_element_by_xpath("//div[@class='open']/ul/li[1]/a/label/input").is_selected():
        wd.find_element_by_xpath("//div[@class='open']/ul/li[1]/a/label/input").click()
    wd.find_element_by_id("BossLastName").click()
    wd.find_element_by_id("BossLastName").clear()
    wd.find_element_by_id("BossLastName").send_keys("sfgsggs")
    wd.find_element_by_id("BossFirstName").click()
    wd.find_element_by_id("BossFirstName").send_keys("\\83")
    wd.find_element_by_id("BossFirstName").click()
    wd.find_element_by_id("BossFirstName").clear()
    wd.find_element_by_id("BossFirstName").send_keys("sgsdgsdg")
    wd.find_element_by_id("BossMiddleName").click()
    wd.find_element_by_id("BossMiddleName").send_keys("\\71")
    wd.find_element_by_id("BossMiddleName").click()
    wd.find_element_by_id("BossMiddleName").clear()
    wd.find_element_by_id("BossMiddleName").send_keys("dsgsdg")
    wd.find_element_by_id("EMailSenderCheck").click()
    wd.find_element_by_id("EMail").click()
    wd.find_element_by_id("EMail").clear()
    wd.find_element_by_id("EMail").send_keys("atolgg@gmail.ru")
    wd.find_element_by_id("EMailSenderCheck").click()
    wd.find_element_by_id("EMailSenderCheck").clear()
    wd.find_element_by_id("EMailSenderCheck").send_keys("atolgg@gmail.ru")
    wd.find_element_by_id("nextButton").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")