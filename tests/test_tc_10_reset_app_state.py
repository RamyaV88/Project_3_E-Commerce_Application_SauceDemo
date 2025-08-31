from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestResetAppState(BaseTest):

    # Test Case - 10: Validate "Reset App State" functionality

    def test_reset_app_state_after_adding_products(self):
        self.logger.info("****** Test Case - 10: Reset App State Test Started ******")
        login_page = LoginPage(self.driver)
        inventory_page = login_page.verify_successful_login(self.username, self.password)
        inventory_page.add_sauce_labs_bike_light()
        inventory_page.add_sauce_labs_bolt_t_shirt()
        self.logger.info("****** Two products added to cart ******")
        self.driver.save_screenshot(".\\screenshots\\" + "TC_10_Cart_Before_ResetAppState.png")
        inventory_page.click_on_burger_menu()
        self.logger.info("****** Clicking on Reset App State ******")
        base_page = BasePage(self.driver)
        base_page.wait_and_click_on_element(inventory_page.reset_app_button_xpath)
        inventory_page.click_on_shopping_cart_link()
        self.logger.info("****** Products removed from cart and cart remains empty ******")
        self.driver.save_screenshot(".\\screenshots\\" + "TC_10_Empty_Cart_After_ResetAppState.png")
        self.logger.info("****** Test Case - 10: Reset App State Test Completed ******")
