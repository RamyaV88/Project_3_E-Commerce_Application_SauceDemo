from pages.BasePage import BasePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage


class CheckoutStepOnePage(BasePage):

    """CheckoutStepOnePage - Child class of BasePage
        Contains locators and WebDriver operations performed on CheckoutStepOnePage."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""
    checkout_step_one_element_xpath = "//span[@class='title']"
    first_name_id = "first-name"
    last_name_id = "last-name"
    postal_code_id = "postal-code"
    continue_button_id = "continue"

    def verify_checkout_step_one(self):
        """Method to verify title of checkout_step_one Page"""
        check_out_message = self.retrieve_element_text("checkout_step_one_element_xpath",
                                                       self.checkout_step_one_element_xpath)
        assert "Checkout: Your Information" in check_out_message

    def enter_first_name(self, first_name):
        """Method to enter first name"""
        self.enter_text(first_name, "first_name_id", self.first_name_id)

    def enter_last_name(self, last_name):
        """Method to enter last name"""
        self.enter_text(last_name, "last_name_id", self.last_name_id)

    def enter_postal_code(self, postal_code):
        """Method to enter postal code"""
        self.enter_text(postal_code, "postal_code_id", self.postal_code_id)

    def enter_checkout_details(self, first_name, last_name, postal_code):
        """Method to enter checkout details"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_on_continue()

    def click_on_continue(self):
        """Method to click on continue button and proceed further"""
        self.element_click("continue_button_id", self.continue_button_id)
        assert "checkout-step-two" in self.driver.current_url
        return CheckoutStepTwoPage(self.driver)
