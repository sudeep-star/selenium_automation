from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class CartPage:
    CART_TITLE=(By.CLASS_NAME,"title")

    PRODUCT_NAMES=(By.CLASS_NAME,"inventory_item_name")

    PRODUCT_PRICES=(By.CLASS_NAME,"inventory_item_price")

    PRODUCT_QUANTITY=(By.CLASS_NAME,"cart_quantity")

    CONTINUE_SHOPPING=(By.ID,"continue-shopping")

    CHECKOUT_BUTTON=(By.ID,"checkout")

    REMOVE_BACKPACK=(By.ID,"remove-sauce-labs-backpack")

    REMOVE_BIKE_LIGHT=(By.ID,"remove-sauce-labs-bike-light")

    REMOVE_TSHIRT=(By.ID,"remove-sauce-labs-bolt-t-shirt")

    CART_BADGE=(By.CLASS_NAME,"shopping_cart_badge")

    CART_ICON=(By.CLASS_NAME,"shopping_cart_link")

    def __init__(self,driver):
        self.driver=driver


    def open_cart(self):
        self.driver.find_element(
            *self.CART_ICON
        ).click()
    def get_cart_title(self):
        return self.driver.find_element(
            *self.CART_TITLE
        ).text
    def get_product_count(self):
        return len(self.driver.find_elements(
            *self.PRODUCT_QUANTITY)
        )
    def get_cart_badge_count(self):
        return self.driver.find_element(
            *self.CART_BADGE
            ).text
    def remove_backpack(self):
        self.driver.find_element(
            *self.REMOVE_BACKPACK
        ).click()
    def remove_tshirt(self):
        self.driver.find_element(
            *self.REMOVE_TSHIRT
        ).click()
    def remove_bike_light(self):
        self.driver.find_element(
        *self.REMOVE_BIKE_LIGHT
    ).click()
    def click_continue_shopping(self):
        self.driver.find_element(
            *self.CONTINUE_SHOPPING
        ).click()
    def click_checkout(self):
            self.driver.find_element(
                *self.CHECKOUT_BUTTON
            ).click()
        
    def get_product_names(self):
        products = self.driver.find_elements(
            *self.PRODUCT_NAMES
        )

        return [product.text for product in products]
    
    def is_product_in_cart(self, product_name):
        return product_name in self.get_product_names()

    def is_cart_empty(self):
        return self.get_product_count() == 0


