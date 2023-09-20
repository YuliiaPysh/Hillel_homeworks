from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_field = lambda: self._driver.find_element(By.ID, 'signupName')
        self.last_name_field = lambda: self._driver.find_element(By.ID, 'signupLastName')
        self.email_field = lambda: self._driver.find_element(By.ID, 'signupEmail')
        self.password_field = lambda: self._driver.find_element(By.ID, 'signupPassword')
        self.repeat_password_field = lambda: self._driver.find_element(By.ID, 'signupRepeatPassword')
        self.register = lambda: self._driver.find_element(By.XPATH, "//button[text()='Register']")
