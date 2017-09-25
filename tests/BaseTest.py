from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:/chromedriver.exe')
        self.driver.maximize_window()

        self.driver.get("http://google.com")

    def tearDown(self):
        self.driver.quit()
        return self
