import allure

from facade.base_facade import BaseFacade


class RegistrationFacade(BaseFacade):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Register user")
    def register_user(self, name, lastname, email, password, repeat_password):
        self._main_page.signin_button().click()
        self._registration_page.name_field().send_keys(name)
        self._registration_page.last_name_field().send_keys(lastname)
        self._registration_page.email_field().send_keys(email)
        self._registration_page.password_field().send_keys(password)
        self._registration_page.repeat_password_field().send_keys(repeat_password)
        self._registration_page.register().click()

    def check_login(self):
        return len(self._garage_page.no_garages()) > 0
