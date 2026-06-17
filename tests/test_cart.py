from pages.cart_page import CartPage
from pages.inventory_pages import InventoryPage
import time
import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_cart_page_loaded(logged_in_driver):

    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)

    
    inventory_pages.open_cart()
    time.sleep(3)
    assert cart_page.get_cart_title() == "Your Cart"

def test_added_product_visible_in_cart(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)

    inventory_pages.add_backpack_to_cart()
    inventory_pages.open_cart()

    assert cart_page.is_product_in_cart(
        "Sauce Labs Backpack"
    )
@pytest.mark.regression
def test_cart_badge_updates(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    #cart_page=CartPage(logged_in_driver)

    inventory_pages.add_backpack_to_cart()
    assert inventory_pages.get_cart_count()== "1"
@pytest.mark.regression
def test_multiple_products_added(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)

    inventory_pages.add_backpack_to_cart()
    time.sleep(10)
    inventory_pages.add_bikelight_to_cart()
    time.sleep(10)
    inventory_pages.add_tshirt_to_cart()
    time.sleep(10)
    inventory_pages.open_cart()
    time.sleep(10)

    assert cart_page.get_product_count()== 3
@pytest.mark.regression
def test_remove_products_from_cart(logged_in_driver):
    inventory_pages=InventoryPage(logged_in_driver)
    cart_page=CartPage(logged_in_driver)

    inventory_pages.add_backpack_to_cart()
    time.sleep(10)
    inventory_pages.add_bikelight_to_cart()
    time.sleep(10)
    inventory_pages.add_tshirt_to_cart()
    time.sleep(10)

    inventory_pages.open_cart()
    time.sleep(10)
    cart_page.remove_backpack()

    assert cart_page.get_product_count()==2

