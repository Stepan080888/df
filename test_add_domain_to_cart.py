from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time
from auftrag_model import Auftrag

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        # self.wd = webdriver.Firefox()
        self.wd = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.wd.get("about:blank")
        self.wd.delete_all_cookies()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, login="K26802", password="dfTestSys0$")
        self.type_domain_name(wd, Auftrag(domain="ilyksthome"))
        self.select_tarif(wd)

    def select_tarif(self, wd):
        # select tariff
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Alle anzeigen'])[1]/preceding::span[2]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Sichern Sie sich Ihren perfekten Domain-Namen'])[1]/following::button[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Nur Domain'])[1]/following::button[1]").click()

    def type_domain_name(self, wd, auftrag):
        # type domain name
        wd.find_element_by_link_text("Neuen Auftrag bestellen").click()
        time.sleep(7)
        wd.find_element_by_name("query").click()
        wd.find_element_by_name("query").clear()
        wd.find_element_by_name("query").send_keys(auftrag.domain)

    def login(self, wd, login, password):
        # login
        wd.find_element_by_css_selector("[name=login]").clear()
        time.sleep(4)
        wd.find_element_by_css_selector("[name=login]").send_keys(login)
        time.sleep(4)
        wd.find_element_by_css_selector("[name=km_password]").clear()
        time.sleep(4)
        wd.find_element_by_css_selector("[name=km_password]").send_keys(password)
        time.sleep(4)
        wd.find_element_by_css_selector("ul.buttongroup button.accept").click()
        time.sleep(10)

        """
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Passwort vergessen?'])[1]/following::button[1]").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Suchbegriff nicht gefunden!'])[1]/following::a[1]").click()
        """

    def open_home_page(self, wd):
        # open login page
        wd.get("https://admin.dftest.eu/kunde/index.php5")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    

    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
