from pages.inventory_pages import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import pytest

def test_checkout_page_loaded(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    inventory_pages.open_cart()
    cart_page.click_checkout()

    assert checkout_page.get_title()=="Checkout: Your Information"
@pytest.mark.regression
def test_empty_fields(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)

    inventory_pages.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_first_name("")
    checkout_page.enter_last_name("")
    checkout_page.enter_zip_code("")

    checkout_page.click_continue_button()

    assert "First Name is required" in checkout_page.get_error_message()   
@pytest.mark.regression
def test_empty_last_name_and_zip(logged_in_driver):

    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)

    inventory_pages.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("")
    checkout_page.enter_zip_code("")

    checkout_page.click_continue_button()

    assert "Last Name is required" in checkout_page.get_error_message()   
@pytest.mark.regression
def test_empty_zip_code(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)

    inventory_pages.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("")

    checkout_page.click_continue_button()

    assert "Postal Code is required" in checkout_page.get_error_message()   

@pytest.mark.smoke
@pytest.mark.regression
def test_valid_checkout(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)

    inventory_pages.open_cart()
    cart_page.click_checkout()

    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")

    checkout_page.click_continue_button()

    assert "checkout-step-two" in logged_in_driver.current_url
    
