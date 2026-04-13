import allure
from pytest import mark
from pages.parameterize_form_simbirsoft_page import FormPage
from utils.data_generator import generate_user


@allure.feature("Form Tests")
class TestForm:

    @allure.title("Позитивный тест отправки формы")
    def test_form_positive(self, browser):
        user = generate_user()
        page = FormPage(browser)

        page.open_page() \
            .fill_name(user["username"]) \
            .fill_password(user["password"]) \
            .select_drinks(["Milk", "Coffee"]) \
            .select_color("Yellow") \
            .select_automation("yes") \
            .fill_email("name@example.com") \
            .fill_message_dynamic() \
            .submit() \
            .verify_alert()

    @allure.title("Негативный тест: пустой email")
    @mark.xfail(reason="Дефект: форма отправляется без email (валидация только на username)")
    def test_form_negative_empty_email(self, browser):
        user = generate_user()
        page = FormPage(browser)

        page.open_page() \
            .fill_name(user["username"]) \
            .fill_password(user["password"]) \
            .select_drinks(["Milk", "Coffee"]) \
            .select_color("Yellow") \
            .select_automation("no") \
            .fill_email("") \
            .fill_message_dynamic() \
            .submit()
        # Передаем False, так как в негативном тесте Alert быть не должно
        page.verify_alert(should_be_present=False)
