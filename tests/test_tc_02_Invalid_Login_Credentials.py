from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class TestInvalidUserLogin(BaseTest):

    # Test Case - 02: Login with Invalid credentials

    def test_invalid_login_credentials(self):
        self.logger.info("****** Test Case - 2: Login test with Invalid Credentials - Started ******")
        login_page = LoginPage(self.driver)
        login_page.login(self.invalid_username, self.password)
        expected_error_msg = "Epic sadface: Username and password do not match any user in this service"
        assert login_page.retrieve_invalid_error_message().__eq__(expected_error_msg)
        self.driver.save_screenshot(".\\screenshots\\" + "TC_02_Error_Message_Invalid_Login_Credentials.png")
        self.logger.info("****** Test Case - 2: Login test with Invalid Credentials - Completed ******")

    # Test Case - 02: Login with Invalid credentials - Empty credentials passed

    def test_empty_login_credentials(self):
        self.logger.info("****** Test Case - 2: Login test with Empty Credentials - Started ******")
        login_page = LoginPage(self.driver)
        login_page.login("", "")
        expected_error_msg = "Epic sadface: Username is required"
        assert login_page.retrieve_empty_credentials_error_message().__eq__(expected_error_msg)
        self.driver.save_screenshot(".\\screenshots\\" + "TC_02_Error_Message_Empty_Login_Credentials.png")
        self.logger.info("****** Test Case - 2: Login test with Empty Credentials - Completed ******")
