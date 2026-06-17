from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_valid_login(driver):
    login_page=LoginPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce")
    
    assert "inventory" in driver.current_url


@pytest.mark.regression
def test_invalid_login(driver):
    login_page=LoginPage(driver)

    login_page.open()

    login_page.login(
        "wrong_username",
        "wrong_password"
    )

    assert (
        "Username and password"
        in login_page.get_error_message())
    
@pytest.mark.regression    
def test_locked_out_user(driver):

    login_page=LoginPage(driver)
    login_page.open()

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    assert (
        "locked out"
        in login_page.get_error_message().lower()
    )