import pytest

from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import excel_utils


class TestDataDrivenLogin(BaseTest):

    # Test Case - 01: To Validate the Login functionality - Data Driven Test - Multiple sets of credentials fetched from an Excel file

    @pytest.mark.parametrize("username,password",
                             excel_utils.get_data_from_excel("testdata/saucedemo_login_data.xlsx", "LoginTest"))
    def test_login_data_driven(self, username, password):
        self.logger.info("****** Test Case - 1: Validating the Login functionality - Data Driven Test - Started ******")
        self.logger.info("****** Fetching multiple credentials from an excel file - Data Driven Test ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(username, password)
        self.logger.info(
            "****** Test Case - 1: Validating the Login functionality - Data Driven Test - Completed ******")

    # Test Case - 02: To Validate the error message displayed for "locked_out_user" - Data Driven Test - Data fetched from an Excel file

    @pytest.mark.parametrize("username,password", excel_utils.get_data_from_excel("testdata/saucedemo_login_data.xlsx",
                                                                                  "LoginLockedOutUser"))
    def test_login_locked_out_user_credentials_data_driven(self, username, password):
        self.logger.info(
            "****** Test Case - 2: Validating error message displayed for locked_out_user - Started ******")
        self.logger.info("****** Fetching credentials from an excel file - Data Driven Test ******")
        login_page = LoginPage(self.driver)
        login_page.login(username, password)
        expected_error_msg = "Epic sadface: Sorry, this user has been locked out."
        assert login_page.retrieve_locked_out_user_error_message().__eq__(expected_error_msg)
        self.logger.info(
            "****** Test Case - 2: Validating error message displayed for locked_out_user - Completed ******")
