from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    PAGE_TITLE=(By.CLASS_NAME,"title")
    COMPLETE_HEADER=(By.CLASS_NAME,"complete-header")
    COMPLETE_TEXT=(By.CLASS_NAME,"complete-text")
    COMPLETE_IMAGE=(By.CLASS_NAME,"pony-express")
    BACK_HOME_BUTTON=(By.ID,"back-to-products")

    def __init__(self,driver):
        self.driver=driver

    def get_page_title(self):
        return self.driver.find_element(
            *self.PAGE_TITLE
        ).text
    def get_complete_header(self):
        return self.driver.find_element(
            *self.COMPLETE_HEADER
        ).text
    def get_complete_text(self):
        return self.driver.find_element(
            *self.COMPLETE_TEXT
        )
    def get_complete_image(self):
        return self.driver.find_element(
            *self.COMPLETE_IMAGE
        )
    def click_back_home(self):
        return self.driver.find_element(
            *self.BACK_HOME_BUTTON
        ).click()

