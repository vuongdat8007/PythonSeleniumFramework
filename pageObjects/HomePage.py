from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ShopPage import ShopPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, 'exampleFormControlSelect1')
    radios = (By.XPATH, "//input[@type='radio']")
    bday = (By.NAME, "bday")
    submit_btn = (By.XPATH, "//input[@type='submit']")
    result_message = (By.CLASS_NAME, 'alert-success')

    # static dropdown

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def pick_gender(self, gender):
        dropdown = Select(self.driver.find_element(*HomePage.gender))
        # dropdown.select_by_index(1)
        dropdown.select_by_visible_text(gender)

    def pick_employment_status(self, option):
        statuses = self.driver.find_elements(*HomePage.radios)
        for status in statuses:
            if status.get_attribute('value') == option:
                if status.is_enabled():
                    status.click()
                    return
                else:
                    raise Exception(f"Employment status for {option} is disabled!")
        raise Exception(f"No employment status for {option}")

    def get_birthday(self):
        return self.driver.find_element(*HomePage.bday)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def result_msg(self):
        return self.driver.find_element(*HomePage.result_message).text