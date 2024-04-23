from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class ConfirmPage:

    country_txt = (By.ID, "country")
    suggestion_popup = (By.XPATH, "//div[@class='suggestions']")
    confirm_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirm_purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_lbl = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
       self.driver = driver

    def get_country_txt(self):
        return self.driver.find_element(*ConfirmPage.country_txt)

    def click_country_link(self, country_name):
        try:
            self.driver.find_element(By.LINK_TEXT, country_name).click()

        except NoSuchElementException:
            raise ValueError(f"Link with text '{country_name}' not found")

    def click_confirm_chkbox(self):
        try:
            self.driver.find_element(*ConfirmPage.confirm_checkbox).click()
        except NoSuchElementException:
            raise ValueError("Confirm checkbox not found on confirm page!")

    def click_confirm_purchase(self):
        try:
            self.driver.find_element(*ConfirmPage.confirm_purchase).click()
        except NoSuchElementException:
            raise ValueError("Purchase button was not found on ShippingPage")

    def get_success_lbl(self):
        try:
            return self.driver.find_element(*ConfirmPage.success_lbl).text
        except NoSuchElementException:
            raise ValueError("Failed to confirm purchase")