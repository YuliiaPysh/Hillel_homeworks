from pages.garage_page import GaragePage
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage


class BaseFacade:
    def __init__(self, driver):
        self._driver = driver
        self._main_page = MainPage(self._driver)
        self._registration_page = RegistrationPage(self._driver)
        self._garage_page = GaragePage(self._driver)

