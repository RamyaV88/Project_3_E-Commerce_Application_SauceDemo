from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.InventoryPage import InventoryPage


class LoginPage(BasePage):

    """CartPage - Child class of BasePage
    Contains locators and WebDriver operations performed on Cart Page."""

    def __init__(self, driver):
        super().__init__(driver)

    # LoginPage Locators
    username_input_id = "user-name"  # Username input field
    password_input_id = "password"  # Password input field
    login_button_id = "login-button"  # Login button field
    login_invalid_error_message = "//h3[contains(text(),'Epic sadface: Username and password do not match a')]"
    login_empty_credentials_error_message = "//h3[normalize-space()='Epic sadface: Username is required']"
    locked_out_user_error_message = "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out')]"

    """Method to enter text on username field"""
    def enter_username_field(self, username):
        self.enter_text(username, "username_input_id", self.username_input_id)

    def enter_password_field(self, password):
        """Method to enter text on password field"""
        self.enter_text(password, "password_input_id", self.password_input_id)

    def click_login_button(self):
        """Method to click on login button"""
        self.element_click("login_button_id", self.login_button_id)

    def login(self, username, password):
        """Method to perform login"""
        self.enter_username_field(username)
        self.enter_password_field(password)
        self.click_login_button()
        return InventoryPage(self.driver)

    def verify_successful_login(self, username, password):
        """Method to check successful login functionality"""
        self.enter_username_field(username)
        self.enter_password_field(password)
        self.click_login_button()
        assert "inventory" in self.get_current_url()
        inventory_page = InventoryPage(self.driver)
        assert inventory_page.is_products_displayed()
        return InventoryPage(self.driver)

    def retrieve_invalid_error_message(self):
        """Method to retrieve error message text"""
        return self.driver.find_element(By.XPATH, self.login_invalid_error_message).text

    def retrieve_empty_credentials_error_message(self):
        """Method to retrieve error message text"""
        return self.driver.find_element(By.XPATH, self.login_empty_credentials_error_message).text

    def retrieve_locked_out_user_error_message(self):
        """Method to retrieve error message text"""
        return self.driver.find_element(By.XPATH, self.locked_out_user_error_message).text
