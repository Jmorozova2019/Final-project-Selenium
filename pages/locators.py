from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
