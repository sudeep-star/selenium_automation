from selenium.webdriver.common.by import By
from utils.logger import LogGenerator

class CheckoutPage:
    logger=LogGenerator.get_logger()
            
    FIRST_NAME=(By.ID,"first-name")
    LAST_NAME=(By.ID,"last-name")
    ZIP_CODE=(By.ID,"postal-code")
    CANCEL_BUTTON=(By.ID,"cancel")
    CONTINUE_BUTTON=(By.ID,"continue")
    PAGE_TITLE=(By.CLASS_NAME,"title")
    ERROR_MESSAGE=(By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self,driver):
        self.driver=driver
    def enter_first_name(self,first_name):
        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys(first_name)
    def enter_last_name(self,last_name):
        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)
    def enter_zip_code(self,zip_code):
        self.driver.find_element(
            *self.ZIP_CODE
        ).send_keys(zip_code)
    def click_cancel_button(self):
        self.driver.find_element(
            *self.CANCEL_BUTTON
        ).click()
    def click_continue_button(self):
        self.logger.info("Continue button clicked")
        self.driver.find_element(
            *self.CONTINUE_BUTTON
        ).click()
    
    def get_title(self):
        return self.driver.find_element(
            *self.PAGE_TITLE
        ).text
    def get_error_message(self):
        return self.driver.find_element(
            *self.ERROR_MESSAGE
        ).text
    