from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.InventoryPage import InventoryPage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from utilities import excel_utils


class TestRandomSelectionCompleteCheckout(BaseTest):

    # Test Case - 08: Complete checkout and validate order

    def test_complete_checkout_validate_order(self):
        self.logger.info("****** Test Case - 8: Complete checkout and validate order - Started ******")
        login_page = LoginPage(self.driver)
        login_page.verify_successful_login(self.username, self.password)
        inventory_page = InventoryPage(self.driver)
        self.logger.info("****** Selecting 4 Random Products ******")
        inventory_page.random_product_selection_data_extraction()
        cart_page = inventory_page.click_on_shopping_cart_link()
        self.driver.save_screenshot(".\\screenshots\\" + "TC_08_Screen_1_Random_Products_Added_To_Cart.png")
        cart_page.click_on_checkout_element()
        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        checkout_step_one_page.enter_checkout_details(
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx", "CheckoutDetails", 2, 1),
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx",
                                  "CheckoutDetails", 2, 2),
            excel_utils.read_data("testdata/saucedemo_login_data.xlsx",
                                  "CheckoutDetails", 2, 3))
        self.driver.save_screenshot(".\\screenshots\\" + "TC_08_Screen_2_Checkout_Details.png")
        checkout_step_two_page = CheckoutStepTwoPage(self.driver)
        checkout_step_two_page.verify_checkout_step_two()
        checkout_step_two_page.verify_checkout_summary_container_displayed()
        checkout_step_two_page.price_total_displayed()
        checkout_step_two_page.click_on_finish_button()
        checkout_step_two_page.verify_success_message()
        self.driver.save_screenshot(".\\screenshots\\" + "TC_08_Screen_3_Success_Message.png")
        self.logger.info("****** Test Case - 8: Complete checkout and validate order - Completed ******")
