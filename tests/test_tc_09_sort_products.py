from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestSortProducts(BaseTest):

    # Test Case - 09: Validate sorting functionality on the products page

    def test_sort_functionality(self):
        self.logger.info("****** Test Case - 9: Validate sorting functionality on the products page - Started ******")
        login_page = LoginPage(self.driver)
        inventory_page = login_page.verify_successful_login(self.username, self.password)
        self.driver.save_screenshot(".\\screenshots\\" + "TC_09_Before_Sort.png")
        inventory_page.click_on_sort_button()
        self.logger.info("****** Sorting - Z to A ******")
        inventory_page.sort_z_to_a()
        inventory_page.click_on_sort_button()
        self.logger.info("****** Sorting : Price - Low to High ******")
        inventory_page.sort_price_high_to_low()
        inventory_page.click_on_sort_button()
        self.logger.info("****** Sorting : A to Z ******")
        inventory_page.sort_a_to_z()
        inventory_page.click_on_sort_button()
        self.logger.info("****** Sorting : Price - High to Low ******")
        inventory_page.sort_price_low_to_high()
        self.logger.info("****** Test Case - 9: Validate sorting functionality on the products page - Started ******")
