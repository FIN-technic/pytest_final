from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Invalid URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        input_password.send_keys(password)
        input_re_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        input_re_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        button.click()
