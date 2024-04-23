from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage


class ShopPage:

    def __init__(self, driver):
       self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    checkoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def getCardTitle(self):
        return self.driver.find_elements(*CartPage.cardTitle)

    def add_to_cart(self, product_name):
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            if product_name in product.find_element(By.XPATH, 'div/h4/a').text:
                return product.find_element(By.XPATH, "div/button").click()
        return None

    def go_to_checkout(self):
        self.driver.find_element(*ShopPage.checkoutBtn).click()
        checkout_page = CheckOutPage(self.driver)
        return checkout_page

