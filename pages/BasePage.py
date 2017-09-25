from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, time=TIMEOUT):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        self.wait_for_element(locator)
        return self.driver.find_elements(*locator)

    def click_on(self, locator):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        element.click()

    def insert_text(self, locator, text):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return self
