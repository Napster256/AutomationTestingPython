import allure
from selenium.webdriver.common.by import By
from ..base_page import BasePage


class MainPage(BasePage):

    URL = "https://vikunja.io/"

    BUTTON_DEMO = (
        By.CSS_SELECTOR, ".py-2.px-4.sm\\:group-hover\\:py-0.transition-all.flex.items-center")

    PROFILE = (By.CSS_SELECTOR,
               ".base-button.base-button--type-button.username-dropdown-trigger")
    LOGOUT = (By.CSS_SELECTOR,
              ".base-button.base-button--type-button.dropdown-item")

    @allure.step("Open Vikunja main page")
    def open_main_page(self):
        self.open(self.URL)

    @allure.step("Click demo button")
    def open_demo(self):
        self.click(self.BUTTON_DEMO)

    @allure.step("Logout from profile")
    def logout(self):
        self.click(self.PROFILE)
        self.click(self.LOGOUT)

    @allure.step("Verify main slogan")
    def verify_slogan(self):
        self.see("Plan your projects with the elegance")
