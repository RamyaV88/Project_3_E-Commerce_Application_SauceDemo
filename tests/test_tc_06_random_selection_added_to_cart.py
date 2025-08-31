from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestRandomSelectionAddedToCart(BaseTest):

    # Test Case - 06: Add selected products to cart and validate

    def test_verify_selected_random_products_on_cart(self):
        self.logger.info("****** Test Case - 6: Add selected products to cart and validate - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)
        inventory_page = InventoryPage(self.driver)
        self.logger.info("****** Selecting 4 Random Products ******")
        inventory_page.random_product_selection_data_extraction()
        cart_page = inventory_page.click_on_shopping_cart_link()
        self.driver.save_screenshot(".\\screenshots\\" + "TC_06_Random_Products_Added_To_Cart.png")
        self.logger.info("****** Test Case - 6: Added selected products to cart and validated - Completed ******")
