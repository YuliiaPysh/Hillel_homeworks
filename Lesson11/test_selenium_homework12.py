from selenium import webdriver
import requests
from facade.registration_facade import RegistrationFacade


class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()
        self._registration_facade = RegistrationFacade(self._driver)

        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")


class TestRegistration(TestBase):
    def setup_class(self):
        self.user_email = "test345678345678ord@gmail.com"
        self.user_password = "Testpassword1"

        self.user = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self):
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")
        self._driver.quit()

    def test_registration(self):
        self._registration_facade.register_user("Nick", "Ivanov", self.user_email, self.user_password, self.user_password)
        assert self._registration_facade.check_login()
