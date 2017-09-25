from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ResultsPage(BasePage):
    RESULTS = (By.CLASS_NAME, 'g')

    def is_query_in_results(self):
        y = 10
        for x in range(10):
            print(x+1)



        return self
