from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.task_page import TaskObjects
from utils.utility import Util


@pytest.fixture(scope='session')
def driver():
    """
    Fixture to initialize webdriver
    :return: driver
    """
    driver_path = str(Path(__file__).parent.parent.joinpath("resources").joinpath("chromedriver.exe"))
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(Util.get_config('base_url'))
    driver.maximize_window()
    yield driver
    clear_todo_list(driver)
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def login_and_open_mytask(driver):
    """
    Fixture to login to the application
    :param driver:
    :return:
    """
    driver.find_element(*TaskObjects.sign_in).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TaskObjects.sign_in_btn))
    driver.find_element(*TaskObjects.user_email).send_keys(Util.get_config("default_uname"))
    driver.find_element(*TaskObjects.user_pwd).send_keys(Util.get_config("default_pwd"))
    driver.find_element(*TaskObjects.sign_in_btn).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(TaskObjects.my_task))
    driver.find_element(*TaskObjects.my_task).click()


def clear_todo_list(driver):
    """
    Tear down method to clear all tasks created.
    :param driver:
    :return:
    """
    get_todo_list = driver.find_elements(*TaskObjects.task_row)
    for each_list in get_todo_list:
        each_list.find_element(*TaskObjects.remove_task_btn).click()
