import pytest
from selenium.webdriver.common.by import By
URL = "http://www.postcard.qa.studio/"

def test_smoke(browser):
    """
   SMK-1. Smoke test
    """

    browser.get(URL)

    button = browser.find_element(By.ID, value="send")
    assert button.text == "Отправить", "unexpected button text"


def test_empty_input_send(browser):
    """
   SMK-2. Negative case
    """

    browser.get(URL)
    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered', "unexpected attribute class"
    button = browser.find_element(By.ID, value="send")
    button.click()
    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered error', "unexpected attribute class"

CARD_INDEX = [
    0,1
]
@pytest.mark.parametrize("index", CARD_INDEX)
@pytest.mark.xfail(reason="unexpected name class selector")
def test_send_postcard(browser, index):
    """
   SMK-3. Positive case
    """

    browser.get(URL)
    prisentButton = browser.find_element(By.ID, value="email")
    prisentButton.click()
    prisentButton.send_keys("digital128ali@gmail.com")
    cards = browser.find_elements(By.CSS_SELECTOR, value="[class*='photo-parent']")
    cards[index].click()
    massage = browser.find_element(By.ID, value="textarea")
    massage.click()
    massage.send_keys("Hello world")
    button = browser.find_element(By.ID, value="send")
    button.click()
    modal = browser.find_element(By.ID, value="modal")
    assert modal.text == "Открытка успешно отправлена!", "unexpected modal text"