import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver
    
    driver.quit()

@pytest.fixture

def logged_in_driver(driver):

    driver.delete_all_cookies()

    login_page=LoginPage(driver)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":

        extra = getattr(report, "extras", [])

        if report.failed:

            driver = item.funcargs.get("logged_in_driver")

            if driver:

                screenshot = f"screenshots/{item.name}.png"

                driver.save_screenshot(screenshot)

                try:
                    from pytest_html import extras

                    extra.append(
                        extras.image(screenshot)
                    )

                except Exception:
                    pass

        report.extras = extra