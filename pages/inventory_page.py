from selenium.webdriver.common.by import By

class InventoryPage:

    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(*self.add_to_cart).click()
