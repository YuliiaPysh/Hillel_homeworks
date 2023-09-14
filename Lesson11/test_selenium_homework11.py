from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestRegistration:

    def setup_class(self):
        self.session = requests.Session()
        self.user_email = "test7763@gmail.com"
        self.user_password = "Testpassword1"

        self.user = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_class(self):
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user)
        self.session.delete(url="https://qauto2.forstudy.space/api/users")

    def test_check_registration(self, driver):
        driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()
        name_field = driver.find_element(By.ID, 'signupName')
        name_field.send_keys("Julia")
        last_name_field = driver.find_element(By.ID, 'signupLastName')
        last_name_field.send_keys("Kravchenko")
        email_field = driver.find_element(By.ID, 'signupEmail')
        email_field.send_keys(self.user_email)
        password_field = driver.find_element(By.ID, 'signupPassword')
        password_field.send_keys(self.user_password)
        repeat_password_field = driver.find_element(By.ID, 'signupRepeatPassword')
        repeat_password_field.send_keys(self.user_password)
        register = driver.find_element(By.XPATH, "//button[text()='Register']")
        register.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='You don’t have any cars in your garage']")))

        url = driver.current_url
        text = driver.find_element(By.XPATH, "//p[text()='You don’t have any cars in your garage']").text
        expected_url = "https://guest:welcome2qauto@qauto2.forstudy.space/panel/garage"

        assert url == expected_url
        assert text == "You don’t have any cars in your garage"
