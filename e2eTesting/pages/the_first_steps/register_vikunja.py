import allure
from selenium.webdriver.common.by import By
from ..base_page import BasePage


class RegisterPage(BasePage):

    LOGIN_URL = "https://try.vikunja.io/login"

    REGISTER_BUTTON = (By.CSS_SELECTOR, "p.mbs-2 a[href='/register']")

    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")

    SUBMIT = (By.ID, "register-submit")

    @allure.step("Open login page")
    def open_login_page(self):
        self.open(self.LOGIN_URL)

    @allure.step("Open register form")
    def open_register_form(self):
        self.click(self.REGISTER_BUTTON)

    @allure.step("Register new user")
    def register_user(self, username, email, password):

        self.open_login_page()
        self.open_register_form()

        self.fill(self.USERNAME, username)
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, password)

        self.click(self.SUBMIT)