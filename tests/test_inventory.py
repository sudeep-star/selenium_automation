from pages.inventory_pages import InventoryPage
from pages.login_page import LoginPage
import time
import pytest

def test_inventory_page_loaded(logged_in_driver):
    
    inventory_pages=InventoryPage(logged_in_driver)
     

    assert inventory_pages.get_page_title()== "Products"

def test_products_are_displayed(logged_in_driver):
    #login_page=LoginPage(driver)
    inventory_pages=InventoryPage(logged_in_driver)
    

    assert inventory_pages.get_product_count()>0

@pytest.mark.smoke
@pytest.mark.regression
def test_products_are_added(logged_in_driver):
    
    inventory_pages=InventoryPage(logged_in_driver)


    inventory_pages.add_backpack_to_cart()
    time.sleep(3)

    assert inventory_pages.get_cart_count() == "1"

@pytest.mark.regression
def test_products_are_removed(logged_in_driver):

    inventory_pages=InventoryPage(logged_in_driver)


    inventory_pages.add_backpack_to_cart()
    time.sleep(3)
    inventory_pages.remove_backpack_to_cart()
    time.sleep(3)
    assert inventory_pages.get_cart_count()== 6

def test_product_details(logged_in_driver):
    
    inventory_pages=InventoryPage(logged_in_driver)


    inventory_pages.get_product_details()

    assert "inventory-item" in logged_in_driver.current_url

def test_open_cart(logged_in_driver):
    
    inventory_pages=InventoryPage(logged_in_driver)

    inventory_pages.open_cart()

    assert "cart" in logged_in_driver.current_url

def test_sort_by_name_az(logged_in_driver):
    
    inventory_pages=InventoryPage(logged_in_driver)

    inventory_pages.sort_by_name_az()
    names=inventory_pages.get_product_names()
    assert names==sorted(names)

def test_sort_by_name_za(logged_in_driver):

    inventory_pages=InventoryPage(logged_in_driver)


    inventory_pages.sort_by_name_za()
    names=inventory_pages.get_product_names()
    assert names==sorted(names,reverse=True)
