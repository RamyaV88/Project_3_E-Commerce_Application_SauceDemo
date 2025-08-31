import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.BasePage import BasePage
from pages.CartPage import CartPage


class InventoryPage(BasePage):

    """InventoryPage - Child class of BasePage
            Contains locators and WebDriver operations performed on InventoryPage."""

    def __init__(self, driver):
        super().__init__(driver)

    """Locators"""
    burger_menu_button_id = "react-burger-menu-btn"
    logout_button_xpath = "//a[@id='logout_sidebar_link']"
    reset_app_button_xpath = "//a[@id='reset_sidebar_link']"
    products_title_xpath = "//span[@class='title']"
    shopping_cart_button_xpath = "//a[@class='shopping_cart_link']"
    cart_badge_xpath = "//span[@class='shopping_cart_badge']"
    products_sort_locator_xpath = "//select[@class='product_sort_container']"
    products_sort_arrow_locator_xpath = "//span[@class='select_container']"

    # Locators - Add to Cart - Products
    add_sauce_labs_backpack_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
    add_sauce_labs_bike_light_xpath = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    add_sauce_labs_bolt_t_shirt_xpath = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    add_sauce_labs_fleece_jacket_xpath = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
    add_sauce_labs_onesie_xpath = "//button[@id='add-to-cart-sauce-labs-onesie']"
    add_test_all_things_tshirt_red_xpath = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    # Locators - Products
    product_sauce_labs_backpack_xpath = "//div[normalize-space()='Sauce Labs Backpack']"
    product_sauce_labs_bolt_t_shirt_xpath = "//div[normalize-space()='Sauce Labs Bolt T-Shirt']"
    product_test_all_things_tshirt_red_xpath = "//div[normalize-space()='Test.allTheThings() T-Shirt (Red)']"
    product_sauce_labs_fleece_jacket_xpath = "//div[normalize-space()='Sauce Labs Fleece Jacket']"
    product_sauce_labs_bike_light_xpath = "//div[normalize-space()='Sauce Labs Bike Light']"
    product_sauce_labs_onesie_xpath = "//div[normalize-space()='Sauce Labs Onesie']"

    # Locators - Product Name and Price

    Product_Name_Sauce_Labs_Backpack_xpath = "//div[@class='inventory_list']/div[1]/div[2]/div[1]/a/div[1]"
    Product_Amount_Sauce_Labs_Backpack_xpath = "//div[@class='inventory_list']/div[1]/div[2]/div[2]/div[1]"
    Product_Name_Sauce_Labs_Bike_Light_xpath = "//div[@class='inventory_list']/div[2]/div[2]/div[1]/a/div[1]"
    Product_Amount_Sauce_Labs_Bike_Light_xpath = "//div[@class='inventory_list']/div[2]/div[2]/div[2]/div[1]"
    Product_Name_Sauce_Labs_Bolt_T_Shirt_xpath = "//div[@class='inventory_list']/div[3]/div[2]/div[1]/a/div[1]"
    Product_Amount_Sauce_Labs_Bolt_T_Shirt_xpath = "//div[@class='inventory_list']/div[3]/div[2]/div[2]/div[1]"
    Product_Name_Sauce_Labs_Fleece_Jacket_xpath = "//div[@class='inventory_list']/div[4]/div[2]/div[1]/a/div[1]"
    Product_Amount_Sauce_Labs_Fleece_Jacket_xpath = "//div[@class='inventory_list']/div[4]/div[2]/div[2]/div[1]"
    Product_Name_Sauce_Labs_Onesie_xpath = "//div[@class='inventory_list']/div[5]/div[2]/div[1]/a/div[1]"
    Product_Amount_Sauce_Labs_Onesie_xpath = "//div[@class='inventory_list']/div[5]/div[2]/div[2]/div[1]"
    Product_Name_Test_allTheThings_T_Shirt_Red_xpath = "//div[@class='inventory_list']/div[6]/div[2]/div[1]/a/div[1]"
    Product_Amount_Test_allTheThings_T_Shirt_Red_xpath = "//div[@class='inventory_list']/div[6]/div[2]/div[2]/div[1]"



    def backpack(self):
        """Method to fetch text of product"""
        backpack = self.retrieve_element_text("product_sauce_labs_backpack_xpath",
                                              self.product_sauce_labs_backpack_xpath)
        return backpack

    def bolt_tshirt(self):
        """Method to fetch text of product"""
        bolt_tshirt = self.retrieve_element_text("product_sauce_labs_bolt_t_shirt_xpath",
                                                 self.product_sauce_labs_bolt_t_shirt_xpath)
        return bolt_tshirt

    def all_things(self):
        """Method to fetch text of product"""
        all_things = self.retrieve_element_text("product_test_all_things_tshirt_red_xpath",
                                                self.product_test_all_things_tshirt_red_xpath)
        return all_things

    def fleece_jacket(self):
        """Method to fetch text of product"""
        fleece_jacket = self.retrieve_element_text("product_sauce_labs_fleece_jacket_xpath",
                                                   self.product_sauce_labs_fleece_jacket_xpath)
        return fleece_jacket

    def bike_light(self):
        """Method to fetch text of product"""
        backpack = self.retrieve_element_text("product_sauce_labs_bike_light_xpath",
                                              self.product_sauce_labs_bike_light_xpath)
        return backpack

    def onesie(self):
        """Method to fetch text of product"""
        onesie = self.retrieve_element_text("product_sauce_labs_onesie_xpath", self.product_sauce_labs_onesie_xpath)
        return onesie

    def random_product_selection_data_extraction(self):
        """Method to make a list of products and to select 4 random products from the entire product list"""
        product_list = []
        backpack_text = self.backpack()
        bolt_tshirt_text = self.bolt_tshirt()
        all_things_text = self.all_things()
        fleece_jacket_text = self.fleece_jacket()
        bike_light_text = self.bike_light()
        onesie_text = self.onesie()
        product_list.append(backpack_text)
        product_list.append(bolt_tshirt_text)
        product_list.append(all_things_text)
        product_list.append(fleece_jacket_text)
        product_list.append(bike_light_text)
        product_list.append(onesie_text)
        print(len(product_list))
        print(product_list)
        num_products_to_select = 4
        random_products = random.sample(product_list, num_products_to_select)
        print(f"Random Products Selected are : {random_products}")

        if backpack_text in random_products:
            print(self.retrieve_element_text("Product_Name_Sauce_Labs_Backpack_xpath",
                                             self.Product_Name_Sauce_Labs_Backpack_xpath))
            print(self.retrieve_element_text("Product_Amount_Sauce_Labs_Backpack_xpath",
                                             self.Product_Amount_Sauce_Labs_Backpack_xpath))
            self.add_sauce_labs_backpack()

        if bike_light_text in random_products:
            print(self.retrieve_element_text("Product_Name_Sauce_Labs_Bike_Light_xpath",
                                             self.Product_Name_Sauce_Labs_Bike_Light_xpath))
            print(self.retrieve_element_text("Product_Amount_Sauce_Labs_Bike_Light_xpath",
                                             self.Product_Amount_Sauce_Labs_Bike_Light_xpath))
            self.add_sauce_labs_bike_light()

        if all_things_text in random_products:
            print(self.retrieve_element_text("Product_Name_Test_allTheThings_T_Shirt_Red_xpath",
                                             self.Product_Name_Test_allTheThings_T_Shirt_Red_xpath))
            print(self.retrieve_element_text("Product_Amount_Test_allTheThings_T_Shirt_Red_xpath",
                                             self.Product_Amount_Test_allTheThings_T_Shirt_Red_xpath))
            self.add_all_things()

        if bolt_tshirt_text in random_products:
            print(self.retrieve_element_text("Product_Name_Sauce_Labs_Bolt_T_Shirt_xpath",
                                             self.Product_Name_Sauce_Labs_Bolt_T_Shirt_xpath))
            print(self.retrieve_element_text("Product_Amount_Sauce_Labs_Bolt_T_Shirt_xpath",
                                             self.Product_Amount_Sauce_Labs_Bolt_T_Shirt_xpath))
            self.add_sauce_labs_bolt_t_shirt()

        if fleece_jacket_text in random_products:
            print(self.retrieve_element_text("Product_Name_Sauce_Labs_Fleece_Jacket_xpath",
                                             self.Product_Name_Sauce_Labs_Fleece_Jacket_xpath))
            print(self.retrieve_element_text("Product_Amount_Sauce_Labs_Fleece_Jacket_xpath",
                                             self.Product_Amount_Sauce_Labs_Fleece_Jacket_xpath))
            self.add_sauce_labs_fleece_jacket()

        if onesie_text in random_products:
            print(self.retrieve_element_text("Product_Name_Sauce_Labs_Onesie_xpath",
                                             self.Product_Name_Sauce_Labs_Onesie_xpath))
            print(self.retrieve_element_text("Product_Amount_Sauce_Labs_Onesie_xpath",
                                             self.Product_Amount_Sauce_Labs_Onesie_xpath))
            self.add_sauce_labs_onesie()

    def click_on_sort_button(self):
        """Method to click on sort button"""
        self.element_click("products_sort_locator_xpath", self.products_sort_locator_xpath)

    def sort_z_to_a(self):
        """Method to click on sort Z to A"""
        sort_dropdown = Select(self.driver.find_element(By.XPATH, self.products_sort_locator_xpath))
        sort_dropdown.select_by_visible_text("Name (Z to A)")
        self.driver.save_screenshot(".\\screenshots\\" + "After_Sort_Z_to_A.png")

    def sort_price_low_to_high(self):
        """Method to click on sort based on price from low to high"""
        sort_dropdown = Select(self.driver.find_element(By.XPATH, self.products_sort_locator_xpath))
        sort_dropdown.select_by_visible_text("Price (low to high)")
        self.driver.save_screenshot(".\\screenshots\\" + "After_Price_Low_to_High_Sort.png")

    def sort_price_high_to_low(self):
        """Method to click on sort based on price from high to low"""
        sort_dropdown = Select(self.driver.find_element(By.XPATH, self.products_sort_locator_xpath))
        sort_dropdown.select_by_visible_text("Price (high to low)")
        self.driver.save_screenshot(".\\screenshots\\" + "After_Price_High_to_Low_Sort.png")

    def sort_a_to_z(self):
        """Method to click on sort A to Z"""
        sort_dropdown = Select(self.driver.find_element(By.XPATH, self.products_sort_locator_xpath))
        sort_dropdown.select_by_visible_text("Name (A to Z)")
        self.driver.save_screenshot(".\\screenshots\\" + "After_Sort_A_to_Z.png")

    def click_on_burger_menu(self):
        """Method to click on burger menu"""
        self.element_click("burger_menu_button_id", self.burger_menu_button_id)

    def click_on_logout_button(self):
        """Method to click on logout button with explicit wait"""
        wait = WebDriverWait(self.driver, 10)
        logout_element = wait.until(EC.presence_of_element_located((By.XPATH, self.logout_button_xpath)))
        logout_element.click()

    def click_on_reset_app_button(self):
        """Method to click on reset app state button with explicit wait"""
        wait = WebDriverWait(self.driver, 10)
        reset_element = wait.until(EC.presence_of_element_located((By.XPATH, self.reset_app_button_xpath)))
        reset_element.click()

    def is_products_displayed(self):
        """Method to check if products are displayed"""
        return self.check_display_status_of_element("products_title_xpath", self.products_title_xpath)

    def click_on_shopping_cart_link(self):
        """Method to click on shopping cart link"""
        self.element_click("shopping_cart_button_xpath", self.shopping_cart_button_xpath)
        cart_page = CartPage(self.driver)
        assert "Your Cart" in cart_page.cart_page_title_displayed()
        return CartPage(self.driver)

    def is_cart_icon_displayed(self):
        """Method to check if cart icon is displayed"""
        return self.check_display_status_of_element("shopping_cart_button_xpath", self.shopping_cart_button_xpath)

    def add_sauce_labs_backpack(self):
        """Method to add product to cart"""
        self.element_click("add_sauce_labs_backpack_xpath", self.add_sauce_labs_backpack_xpath)

    def add_sauce_labs_bike_light(self):
        """Method to add product to cart"""
        self.element_click("add_sauce_labs_bike_light_xpath", self.add_sauce_labs_bike_light_xpath)

    def add_sauce_labs_bolt_t_shirt(self):
        """Method to add product to cart"""
        self.element_click("add_sauce_labs_bolt_t_shirt_xpath", self.add_sauce_labs_bolt_t_shirt_xpath)

    def add_sauce_labs_fleece_jacket(self):
        """Method to add product to cart"""
        self.element_click("add_sauce_labs_fleece_jacket_xpath", self.add_sauce_labs_fleece_jacket_xpath)

    def add_sauce_labs_onesie(self):
        """Method to add product to cart"""
        self.element_click("add_sauce_labs_onesie_xpath", self.add_sauce_labs_onesie_xpath)

    def add_all_things(self):
        """Method to add product to cart"""
        self.element_click("add_test_all_things_tshirt_red_xpath", self.add_test_all_things_tshirt_red_xpath)
