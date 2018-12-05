import time
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from library.GetData import get_csv_data


@ddt
class TestSceanarioA(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="webdrivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @data(*get_csv_data("data/scenario_a.csv"))
    @unpack
    def test_login(self, target_url, usn_value, pass_value):
        driver = self.driver
        driver.get(target_url)
        login_page = LoginPage(driver)
        login_page.enter_username(usn_value)
        login_page.enter_password(pass_value)
        login_page.click_login_button()
        homepage = HomePage(driver)
        try:
            homepage.click_logout_button()
        except NoSuchElementException:
            print("Login Failed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
