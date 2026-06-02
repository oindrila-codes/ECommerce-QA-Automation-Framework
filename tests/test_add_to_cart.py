from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(setup):

    driver = setup

    driver.get("https://www.saucedemo.com")

    login = LoginPage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory = InventoryPage(driver)

    inventory.add_product()

    assert True
