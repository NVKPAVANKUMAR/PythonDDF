import time
import unittest
from selenium import webdriver
from ddt import ddt, data, unpack
from selenium.common.exceptions import NoSuchElementException

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
        username_input_elem = driver.find_element_by_id('MemberLoginForm_LoginForm_Email')
        username_input_elem.clear()
        username_input_elem.send_keys(usn_value)
        password_input_elem = driver.find_element_by_id('MemberLoginForm_LoginForm_Password')
        password_input_elem.clear()
        password_input_elem.send_keys(pass_value)
        login_button_elem = driver.find_element_by_id('MemberLoginForm_LoginForm_action_doLogin')
        login_button_elem.click()
        time.sleep(5)
        try:
            logout_button_elem = driver.find_element_by_xpath('//*[@id="cms-menu"]/div[1]/div[2]/a[2]')
            logout_button_elem.click()
        except NoSuchElementException:
            print("Login Failed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
