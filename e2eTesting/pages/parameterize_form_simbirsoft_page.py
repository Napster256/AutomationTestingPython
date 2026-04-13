import allure
from pytest import fail
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage


class FormPage(BasePage):

    URL = "https://practice-automation.com/form-fields/"

    NAME = (By.ID, "name-input")
    PASSWORD = (By.CSS_SELECTOR, "#feedbackForm input[type=password]")
    # генерируем локатор по значению, не храним элемент
    def drink_checkbox(self, drink_name: str):
        return (By.XPATH, f"//input[@value='{drink_name}']")

    def color_radio(self, color_name: str):
        return (By.XPATH, f"//input[@value='{color_name}']")

    LIKE_AUTOMATION = (By.ID, "automation")

    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")

    AUTOMATION_TOOLS = (By.XPATH, "//form[@id='feedbackForm']/ul/li")

    @allure.step("Открыть страницу формы")
    def open_page(self):
        self.open(self.URL)
        return self

    @allure.step("Заполнить имя: {name}")
    def fill_name(self, name):
        self.fill(self.NAME, name)
        return self

    @allure.step("Заполнить пароль")
    def fill_password(self, password):
        self.fill(self.PASSWORD, password)
        return self

    @allure.step("Выбрать напитки: {drinks}")
    def select_drinks(self, drinks: list):
        for drink in drinks:
            locator = self.drink_checkbox(drink)
            element = self.browser.find_element(*locator)
            self.browser.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        return self

    @allure.step("Выбрать цвет: {color}")
    def select_color(self, color):
        self.click(self.color_radio(color))
        return self

    @allure.step("Выбрать вариант автоматизации: {option}")
    def select_automation(self, option="yes"):
        dropdown = Select(self.browser.find_element(*self.LIKE_AUTOMATION))
        dropdown.select_by_value(option.lower())
        return self

    @allure.step("Заполнить email: {email}")
    def fill_email(self, email):
        self.fill(self.EMAIL, email)
        return self

    @allure.step("Сформировать сообщение")
    def fill_message_dynamic(self):
        tools = self.browser.find_elements(*self.AUTOMATION_TOOLS)
        tools_texts = [tool.text for tool in tools]

        count = len(tools_texts)
        longest_tool = max(tools_texts, key=len)

        message = f"{count} tools. Longest: {longest_tool}"
        self.fill(self.MESSAGE, message)
        return self

    @allure.step("Нажать Submit")
    def submit(self):
        element = self.browser.find_element(*self.SUBMIT)
        self.browser.execute_script("arguments[0].click();", element)
        return self

    @allure.step("Проверить алерт")
    def verify_alert(self, should_be_present=True):
        try:
            alert = self.browser.switch_to.alert
            text = alert.text
            if not should_be_present:
                alert.accept()
                fail(
                    f"«Обнаружен дефект: форма отправлена с пустым полем Email. Получен алерт: '{text}'. Валидация срабатывает только при отсутствии Username»")
            allure.attach(text, name="Alert text",
                          attachment_type=allure.attachment_type.TEXT)

            assert text == "Message received!"
            alert.accept()
        except NoAlertPresentException:
            # Если alert был нужен (True) — кидаем ошибку.
            # Если alert отсутствует (False) — всё ок, тест прошел
            if should_be_present:
                fail("Форма не была отправлена, (alert не появился)")
