from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from utils.logger import LogGenerator

class InventoryPage:
    logger=LogGenerator.get_logger()
    URL = "https://www.saucedemo.com/inventory.html"

    PAGE_TITLE=(
        By.CLASS_NAME,
        "title"
    )

    CART_ICON =(
        By.CLASS_NAME,
        "shopping_cart_link"
    )
    CART_BADGE=(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )
    BACKPACK_ADD_BUTTON=(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    BACKPACK_REMOVE_BUTTON=(
        By.ID,
        "remove-sauce-labs-backpack"
    )

    BIKELIGHT_ADD_BUTTON=( # type: ignore
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    )

    TSHIRT_ADD_BUTTON=(
        By.ID,
        "add-to-cart-sauce-labs-bolt-t-shirt"
    )
    PRODUCT_NAMES=(
        By.CLASS_NAME,
        "inventory_item_name"
    )
    PRODUCT_PRICES=(
        By.CLASS_NAME,
        "inventory_item_price"
    )
    SORT_DROPDOWN=(
        By.CLASS_NAME,
        "product_sort_container"
    )

    def __init__(self,driver):
        self.driver=driver
 #validations

    def get_page_title(self):
        return self.driver.find_element(
            *self.PAGE_TITLE
        ).text
   
    def get_product_count(self):
        return len(
            self.driver.find_elements(
                *self.PRODUCT_NAMES
            )
        )
    
    
    #cart actions

    def add_backpack_to_cart(self):
        self.logger.info("Adding backpack to cart")
        self.driver.find_element(
            *self.BACKPACK_ADD_BUTTON
        ).click()
    def remove_backpack_to_cart(self):
        self.logger.info("Removing backpack from cart")
        self.driver.find_element(
            *self.BACKPACK_REMOVE_BUTTON
        ).click()
    
    def add_bikelight_to_cart(self):
        self.driver.find_element(
            *self.BIKELIGHT_ADD_BUTTON
        ).click()
    
    def add_tshirt_to_cart(self):
        self.driver.find_element(
            *self.TSHIRT_ADD_BUTTON
        ).click()
    
    def get_cart_count(self):
        badges= self.driver.find_element(
            *self.CART_BADGE
        )
        if len(badges)==0:
            return 0
        else:
            return int(badges[0].text)
    
    
    def open_cart(self):
        self.driver.find_element(
            *self.CART_ICON
        ).click()
    
    #product data

    def get_product_names(self):
        products= self.driver.find_elements(
            *self.PRODUCT_NAMES
        )
        return [product.text for product in products]

    def get_product_prices(self):
        prices= self.driver.find_elements(
            *self.PRODUCT_PRICES
        )
        return [price.text for price in prices]

    def is_inventory_page_loaded(self):

        return self.driver.current_url == self.URL
    
    def get_product_details(self):
        self.driver.find_element(
            *self.PRODUCT_NAMES
        ).click()
    
    def sort_by_name_az(self):
        Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        ).select_by_visible_text(
            "Name (A to Z)"
        )

    def sort_by_name_za(self):
        Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        ).select_by_visible_text(
            "Name (Z to A)"
        )

    def sort_by_price_low_high(self):
        Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        ).select_by_visible_text(
            "Price (low to high)"
        )

    def sort_by_price_high_low(self):
        Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        ).select_by_visible_text(
            "Price (high to low)"
        )