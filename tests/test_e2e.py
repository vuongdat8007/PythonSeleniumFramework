import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

from pageObjects.ShopPage import ShopPage
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # //a[@contains(href, 'shop')] : doesnt work
        # driver.find_element(By.CSS_SELECTOR, "a[@contains(href, 'shop')]").click()
        driver = self.driver

        #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        homePage = HomePage(self.driver)
        shop_page = homePage.shopItems()
        log.info("Open shop page - getting all the card items")
        # print(driver.title)
        # print(driver.find_element(By.CSS_SELECTOR, "h1[class='my-4']").text)

        # homePage.get_product("Blackberry").click()

        #checkoutPage = CheckOutPage(self.driver)
        shop_page.add_to_cart("Blackberry")
        log.info("pick product Blackberry to add to cart")
        # explicit wait
        # wait = WebDriverWait(driver, 10)
        # wait.until(expected_conditions.presence_of_element_located(shop_page.checkoutBtn))
        # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        #checkout_page.check_out_items().click()
        #cart_page = CartPage(self.driver)
        checkout_page = shop_page.go_to_checkout()

        # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        shipping_page = checkout_page.confirm_cart()

        # driver.find_element(By.ID, "country").send_keys("V")
        # shipping_page = ConfirmPage(self.driver)

        shipping_page.get_country_txt().send_keys("V")

        # wait.until(expected_conditions.presence_of_element_located(shipping_page.suggestion_popup))

        self.wait_for_element((By.XPATH, "//div[@class='suggestions']"))

        # driver.find_element(By.LINK_TEXT, "Slovakia").click()
        shipping_page.click_country_link("Slovakia")

        # driver.find_element(By.XPATH, "//input[@id='checkbox2']").click() @ WHY ???
        # driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        shipping_page.click_confirm_chkbox()

        #driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()
        shipping_page.click_confirm_purchase()
        successText = shipping_page.get_success_lbl()
        # successText = driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info(f"Text receive from web is {successText}")
        assert ('Success! Thank you' in successText)
