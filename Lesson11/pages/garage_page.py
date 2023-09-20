from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GaragePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.no_garages = lambda: self._driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")
