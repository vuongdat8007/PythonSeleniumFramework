import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_for_element(self, tuple_element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(tuple_element))

    def verify_link_presence(self, link_text):
        element = (WebDriverWait(self.driver, 10)
                   .until(EC.presence_of_element_located((By.LINK_TEXT, link_text))))

    def select_option_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)  # __name__ to capture testcase name
        logger = logging.getLogger(loggerName) # __name__ to capture testcase name which called this class
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object

        logger.setLevel(logging.DEBUG)  # set level of logging to log
        return logger