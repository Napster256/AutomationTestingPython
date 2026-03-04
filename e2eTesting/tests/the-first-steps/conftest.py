import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def browser():
    """
    Fixture for setting up a browser instance for tests.

    This fixture sets up a Chrome browser instance with the following options:
    - no sandbox
    - start maximized
    - disable info bars
    - disable extensions

    The browser instance is set up before the test session starts and is
    torn down after the test session finishes.

    Yields a webdriver.Chrome instance.
    """

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
    yield browser
    browser.quit()
