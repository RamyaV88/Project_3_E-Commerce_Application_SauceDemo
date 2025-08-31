from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestCartVisibility(BaseTest):

    # Test Case - 04: Check cart icon visibility

    def test_cart_visibility(self):
        self.logger.info("****** Test Case - 4: Cart Icon Visibility Test - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)
        inventory_page = InventoryPage(self.driver)
        inventory_page.is_cart_icon_displayed()
        self.driver.save_screenshot(".\\screenshots\\" + "TC_04_Cart_Visibility.png")
        self.logger.info("****** Checking if cart icon is visible ******")
        self.logger.info("****** Test Case - 4: Cart Icon Visibility Test - Completed ******")
