from selenium.webdriver.common.by import By
from utils.logger import LogGenerator

class LoginPage:
    logger=LogGenerator.get_logger()
    URL = "https://www.saucedemo.com"

    USERNAME=(By.ID,"user-name")
    PASSWORD=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"login-button")

    ERROR_MESSAGE=(By.CSS_SELECTOR,
                   "h3[data-test='error']")

    def __init__(self,driver):
        self.driver=driver
    
    def open(self):
        self.driver.get(self.URL)
    
    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
    def click_login(self):
        self.logger.info("Login Button Clicked")
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, username, password):
        self.logger.info(f"Logging in with {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
