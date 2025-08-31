from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestRandomSelectionDataExtraction(BaseTest):

    # Test Case - 05: Random selection of products and data extraction

    def test_selecting_random_products_data_extraction(self):
        self.logger.info("****** Test Case - 5: Random selection of products and data extraction Test - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)
        inventory_page = InventoryPage(self.driver)
        self.logger.info("****** Selecting 4 Random Products ******")
        inventory_page.random_product_selection_data_extraction()
        self.logger.info(
            "****** Test Case - 5: Random selection of products and data extraction Test - Completed ******")
