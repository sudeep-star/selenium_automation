from selenium.webdriver.common.by import By

class CheckoutOverviewPage:

    PAGE_TITLE=(By.CLASS_NAME,"title")
    PRODUCT_NAMES=(By.CASS_NAME,"inventory_item_name")
    PRODUCT_PRICES=(By.CLASS_NAME,"inventory_item_price")
    ITEM_TOTAL=(By.CLASS_NAME,"summary_subtotal_label")
    TAX=(By.CLASS_NAME,"summary_tax_label")
    TOTAL_PRICE=(By.CLASS_NAME,"summary_total_label")
    FINISH_BUTTON=(By.ID,"finish")
    CANCEL_BUTTON=(By.ID,"cancel")

    def __init__(self,driver):
        self.driver=driver

    def get_page_title(self):
        return self.driver.find_element(
            *self.PAGE_TITLE
        ).text
    def get_product_name(self):
        products=self.driver.find_elements(
            *self.PRODUCT_NAMES
        )
        return [product.text for product in products]
    def get_total_item(self):
        return self.driver.find_element(
            *self.ITEM_TOTAL
        )
    def get_product_prices(self):
        return self.driiver.find_element(
            *self.PRODUCT_PRICES
        )
    def get_tax(self):
        return self.driver.find_element(
            *self.TAX
        )
    def get_total_price(self):
        return self.driver.find_element(
            *self.TOTAL_PRICE
        )
    def finish_button(self):
        return self.driver.find_element(
            *self.FINISH_BUTTON
        ).click()
    def cancel_button(self):
        return self.driver.find_element(
            *self.CANCEL_BUTTON
        ).click()
    def get_product_count(self):
        return len(
            self.driver.find_elements(
                *self.PRODUCT_NAMES
            )
        )
    def is_product_present(self,product_name):
        return product_name in self.get_product_name()

