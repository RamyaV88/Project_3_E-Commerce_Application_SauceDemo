from pages.BasePage import BasePage


class CheckoutStepTwoPage(BasePage):

    """CheckoutStepOnePage - Child class of BasePage
            Contains locators and WebDriver operations performed on CheckoutStepOnePage."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""
    checkout_step_two_element_xpath = "//span[@class='title']"
    price_total_field_xpath = "//div[normalize-space()='Price Total']"
    finish_button_id = "finish"
    success_message_xpath = "//h2[normalize-space()='Thank you for your order!']"
    checkout_summary_container_id = "checkout_summary_container"

    def verify_checkout_summary_container_displayed(self):
        """Method to verify checkout summary on checkout_step_two Page"""
        self.check_display_status_of_element("checkout_summary_container_id", self.checkout_summary_container_id)

    def verify_checkout_step_two(self):
        """Method to verify title of checkout_step_two Page"""
        assert "Checkout: Overview".__eq__(
            self.retrieve_element_text("checkout_step_two_element_xpath", self.checkout_step_two_element_xpath))

    def price_total_displayed(self):
        """Method to verify total price on checkout_step_two Page"""
        self.check_display_status_of_element("price_total_field_xpath", self.price_total_field_xpath)

    def click_on_finish_button(self):
        """Method to click on finish button and proceed further"""
        self.element_click("finish_button_id", self.finish_button_id)
        assert "checkout-complete" in self.driver.current_url

    def verify_success_message(self):
        """Method to verify success message - confirmation"""
        success_message = self.retrieve_element_text("success_message_xpath", self.success_message_xpath)
        assert success_message.__eq__("Thank you for your order!")

