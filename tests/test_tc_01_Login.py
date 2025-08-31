from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestLogin(BaseTest):

    # Test Case - 01: Login with various predefined users [standard_user, problem_user, performance_glitch_user, error_user, visual_user, locked_out_user]

    def test_valid_login_standard_user(self):
        self.logger.info("****** Test Case - 1: Login test with various predefined users - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)

    def test_valid_login_problem_user(self):
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.problem_user, self.password)

    def test_valid_login_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.performance_glitch_user, self.password)

    def test_valid_login_error_user(self):
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.error_user, self.password)

    def test_valid_login_visual_user(self):
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.visual_user, self.password)

    def test_login_locked_out_user_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login(self.locked_out_user, self.password)
        expected_error_msg = "Epic sadface: Sorry, this user has been locked out."
        assert login_page.retrieve_locked_out_user_error_message().__eq__(expected_error_msg)
        self.logger.info("****** Test Case - 1: Login test with various predefined users - Completed ******")
