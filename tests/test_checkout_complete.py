from pages.checkout_overview_page import CheckoutOverviewPage
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.inventory_pages import InventoryPage
from pages.checkout_page import CheckoutPage
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_checkout_complete_page_loaded(logged_in_driver):
    inventory_page=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_overview=CheckoutOverviewPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("sudeep")
    checkout_page.enter_last_name("adhikary")
    checkout_page.enter_zip_code("123")

    checkout_page.click_continue_button()
    checkout_overview.finish_button()

    assert "checkout-complete" in logged_in_driver.current_url
@pytest.mark.regression
def test_success_message_displayed(logged_in_driver):
    inventory_page=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_overview=CheckoutOverviewPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_complete=CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("sudeep")
    checkout_page.enter_last_name("adhikary")
    checkout_page.enter_zip_code("123")

    checkout_page.click_continue_button()
    checkout_overview.finish_button()

    assert "Thank you" in checkout_complete.get_complete_header()
@pytest.mark.regression
def test_success_image_displayed(logged_in_driver):
    inventory_page=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_overview=CheckoutOverviewPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_complete=CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("sudeep")
    checkout_page.enter_last_name("adhikary")
    checkout_page.enter_zip_code("123")

    checkout_page.click_continue_button()
    checkout_overview.finish_button()

    assert checkout_complete.is_success_icon_displayed()

def test_click_back_to_home_button(logged_in_driver):
    inventory_page=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)
    checkout_overview=CheckoutOverviewPage(logged_in_driver)
    checkout_page=CheckoutPage(logged_in_driver)
    checkout_complete=CheckoutCompletePage(logged_in_driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    cart_page.click_checkout()
    checkout_page.enter_first_name("sudeep")
    checkout_page.enter_last_name("adhikary")
    checkout_page.enter_zip_code("123")

    checkout_page.click_continue_button()
    checkout_overview.finish_button()
    checkout_complete.click_back_home()

    assert "inventory" in logged_in_driver.current_url


    