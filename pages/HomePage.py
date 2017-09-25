from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.ResultsPage import ResultsPage


class HomePage(BasePage):

    SEARCH = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    LOGO = (By.ID, 'hplogo')

    def type_query(self, text):
        self.insert_text(self.SEARCH, text)
        self.click_on(self.LOGO)
        return self

    def click_on_search_button(self):
        self.click_on(self.SEARCH_BUTTON)
        return ResultsPage(self.driver)
