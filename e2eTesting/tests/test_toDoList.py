import json
import os
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://todomvc.com/examples/emberjs/todomvc/dist/"


def load_tasks():
    current_dir = os.path.dirname(__file__)
    project_root = os.path.join(current_dir, "../")
    static_dir = os.path.join(project_root, "static")
    file_path = os.path.join(static_dir, "tasks.json")

    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


TASKS = load_tasks()
@allure.feature("Functional testing of the task list")
@allure.story("Add single specific task")
def test_add_one_specific_task(browser):

    with allure.step("Open TodoMVC page"):
        browser.get(URL)
        assert "todos" in browser.page_source

    with allure.step("Add task 'Become rich'"):
        input_field = browser.find_element(By.CSS_SELECTOR, "input.new-todo")
        input_field.send_keys("Become rich")
        input_field.send_keys(Keys.ENTER)

    with allure.step("Verify task added"):
        tasks = browser.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        assert any("Become rich" in task.text for task in tasks)


@allure.feature("Functional testing of the task list")
@allure.story("Add multiple tasks from JSON")
@pytest.mark.parametrize("task", TASKS)
def test_add_multiple_tasks(browser, task):

    with allure.step("Open TodoMVC page"):
        browser.get(URL)

    with allure.step(f"Add task: {task}"):
        input_field = browser.find_element(By.CSS_SELECTOR, "input.new-todo")
        input_field.clear()
        input_field.send_keys(task)
        input_field.send_keys(Keys.ENTER)

    with allure.step("Verify task added"):
        tasks = browser.find_elements(By.CSS_SELECTOR, "ul.todo-list li")
        assert any(task in t.text for t in tasks)