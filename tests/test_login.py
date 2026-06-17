from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
@pytest.mark.regression
#@pytest.mark.parametrize(
    #"username,password",[
        #("standard_user","secret_sauce"),
        #("locked_out_user","secret_sauce"),
        ##])
def test_valid_login(driver):
    login_page=LoginPage(driver)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce")
    login_page.login()
    
    assert "inventory" in driver.current_url


@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password",[
        ("",""),
        ("standard_user",""),
        ("","secret_sauce"),
        
    ])
@pytest.mark.sanity
def test_invalid_login(driver,username,password):
    login_page=LoginPage(driver)

    login_page.open()

    #login_page.login(
        #"wrong_username",
        #"wrong_password"
    #)
    login_page.login(username,password)

    #assert (
        #"Username and password"
        #in login_page.get_error_message())
    assert login_page.get_error_message() != ""
    
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