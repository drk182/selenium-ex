from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class SearchTests(BaseTest):
    def test_search_query(self):

        homepage = HomePage(self.driver)
        query = "Query"

        test = (homepage.type_query(query)
                .click_on_search_button()
                .is_query_in_results())

        self.assertTrue(test)
