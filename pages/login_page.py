from .base_page import BasePage
from .locators import LoginPageLocators
import time

LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_elem = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        email_elem.send_keys(email)

        password_elem = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTRATION)
        password_elem.send_keys(password)

        confirm_password_elem = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTRATION)
        confirm_password_elem.send_keys(password)

        register_elem = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        register_elem.click()
        time.sleep(20)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверить корректность url адреса
        assert 'login' in self.browser.current_url, 'URL login incorrect'

    def should_be_login_form(self):
        # Проверить, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # Проверить, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
