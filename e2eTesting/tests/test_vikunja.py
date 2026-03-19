import allure
from pages.main_vikunja import MainPage
from pages.register_vikunja import RegisterPage
from utils.data_generator import generate_user


@allure.feature("Vikunja ToDo")
class TestVikunja:

    @allure.title("Welcome to current issues page in demo")
    def test_welcome_demo(self, browser):

        main_page = MainPage(browser)

        main_page.open_main_page()
        main_page.verify_slogan()
        main_page.open_demo()

        main_page.see('Текущие задачи')

        main_page.logout()

    @allure.title("User registration")
    def test_registration(self, browser):

        register_page = RegisterPage(browser)

        user = generate_user()

        register_page.register_user(
            user["username"],
            user["email"],
            user["password"]
        )

        assert user["username"] in browser.page_source
