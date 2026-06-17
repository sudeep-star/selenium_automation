from pages.cart_page import CartPage
from pages.inventory_pages import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
import time
import pytest

def test_checkout_overview_page_loaded(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    #checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    inventory_pages.open_cart()

    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert "checkout" in logged_in_driver.current_url
@pytest.mark.regression
def test_product_displayed_in_overview(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.open_cart()
    #inventory_pages.add_bikelight_to_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert checkout_overview_page.is_product_present("Sauce Labs Backpack")
@pytest.mark.regression
def test_multiple_product_displayed_in_overview(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert checkout_overview_page.get_product_count()==2

def test_item_total_displayed(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert "Item total" in checkout_overview_page.get_total_item()

def test_tax_displayed(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert "Tax" in checkout_overview_page.get_tax()

def test_total_displayed(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()

    assert "Total" in checkout_overview_page.get_total_price()

@pytest.mark.smoke
@pytest.mark.regression

def test_click_finish_button(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()
    checkout_overview_page.finish_button()

    assert "checkout-complete" in logged_in_driver.current_url

def test_click_cancel_button(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_overview_page=CheckoutOverviewPage(logged_in_driver)

    
    
    inventory_pages.add_backpack_to_cart()
    inventory_pages.add_bikelight_to_cart()
    inventory_pages.open_cart()
    
    cart_page.click_checkout()
    checkout_page.enter_first_name("Sudeep")
    checkout_page.enter_last_name("Adhikary")
    checkout_page.enter_zip_code("123")
    checkout_page.click_continue_button()
    checkout_overview_page.cancel_button()

    assert "inventory" in logged_in_driver.current_url