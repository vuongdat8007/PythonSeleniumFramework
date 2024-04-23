from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    confirm_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def confirm_cart(self):
        self.driver.find_element(*CheckOutPage.confirm_btn).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
