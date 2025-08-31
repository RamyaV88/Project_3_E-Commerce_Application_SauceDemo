from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import excel_utils


class TestRandomSelectionVerifyProductDetails(BaseTest):

    # Test Case - 07: Validate product details inside the cart

    def test_validate_product_details_inside_cart(self):
        self.logger.info("****** Test Case - 7: Validate product details inside the cart - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)
        inventory_page = InventoryPage(self.driver)
        self.logger.info("****** Selecting 4 Random Products ******")
        inventory_page.random_product_selection_data_extraction()
        cart_page = inventory_page.click_on_shopping_cart_link()
        self.driver.save_screenshot(".\\screenshots\\" + "TC_07_Screen_1_Random_Products_Added_To_Cart.png")
        cart_page.click_on_checkout_element()
        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        checkout_step_one_page.enter_checkout_details(
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx", "CheckoutDetails", 2, 1),
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx",
                                  "CheckoutDetails", 2, 2),
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx",
                                  "CheckoutDetails", 2, 3))
        self.driver.save_screenshot(".\\screenshots\\" + "TC_07_Screen_2_Checkout_Details.png")
        checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        checkout_step_two_page.verify_checkout_step_two()
        self.logger.info("****** Test Case - 7: Validated product details inside the cart - Completed ******")
