from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestLogout(BaseTest):

    # Test Case - 03: Validate logout functionality

    def test_tc_03_logout_button(self):
        self.logger.info("****** Test Case - 3: Logout Functionality Test Started ******")
        login_page = LoginPage(self.driver)
        inventory_page = login_page.verify_successful_login(self.username, self.password)
        inventory_page.click_on_burger_menu()
        self.logger.info("****** Clicking on Logout button ******")
        inventory_page.click_on_logout_button()
        self.logger.info("****** Test Case - 3: Logout Functionality Test Completed ******")
