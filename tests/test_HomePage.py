import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, get_data):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info(f"firstname is {get_data["first_name"]}")
        home_page.get_name().send_keys(get_data["first_name"] + get_data["last_name"])
        log.info(f"lastname is {get_data["last_name"]}")
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_password().send_keys(get_data["password"])
        home_page.get_checkbox().click()
        home_page.pick_gender(get_data["gender"])
        self.select_option_by_text(home_page.get_gender(), get_data["gender"])
        home_page.pick_employment_status(get_data["employment_status"])
        home_page.get_birthday().send_keys(get_data["dob"])
        home_page.get_submit_btn().click()
        log.info(f"Message received: {home_page.result_msg()}")
        assert ("Success" in home_page.result_msg())
        self.driver.refresh()

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello agains!")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        # time.sleep(2)

    @pytest.fixture(params=HomePageData.getTestData("testcase-2"))
    def get_data(self, request):
        return request.param