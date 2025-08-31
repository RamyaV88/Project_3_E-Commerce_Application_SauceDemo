from pages.BasePage import BasePage
from pages.CheckoutStepOnePage import CheckoutStepOnePage


class CartPage(BasePage):

    """CartPage - Child class of BasePage
    Contains locators and WebDriver operations performed on Cart Page."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""

    cart_page_title_xpath = "//span[@class='title']"
    remove_sauce_labs_backpack_xpath = "//button[@id='remove-sauce-labs-backpack']"
    checkout_button_id = "checkout"

    """Methods on Cart Page"""

    def cart_page_title_displayed(self):
        """Method to return title on Cart Page"""
        return self.retrieve_element_text("cart_page_title_xpath", self.cart_page_title_xpath)

    def click_on_checkout_element(self):
        """Method to click on checkout element on Cart Page"""
        self.element_click("checkout_button_id", self.checkout_button_id)
        assert "checkout-step-one" in self.driver.current_url
        return CheckoutStepOnePage(self.driver)
