from pages.task_page import TaskObjects
from utils.utility import Util

util = Util()


def test_task_name_less_than_3(driver):
    """
    Test task does not accept less than 3 characters
    :param driver:
    :return:
    """
    task_name = util.generate_random_chars(2)
    driver.find_element(*TaskObjects.create_newtask).send_keys(task_name)
    driver.find_element(*TaskObjects.add_task_icon).click()
    todolist_table = driver.find_elements(*TaskObjects.task_table)
    for list in todolist_table:
        assert list.text != task_name, "Task is created with name less than 3 characters"


def test_task_name_more_than_250(driver):
    """
    Test task does not accept more than 250 characters
    :param driver:
    :return:
    """
    task_name = util.generate_random_chars(252)
    driver.find_element(*TaskObjects.create_newtask).send_keys(task_name)
    driver.find_element(*TaskObjects.add_task_icon).click()
    todolist_table = driver.find_elements(*TaskObjects.task_table)
    for list in todolist_table:
        assert list.text != task_name, "Task is created with name more that 250 characters"


def test_task_name_empty(driver):
    """
    Test task description is mandatory
    :param driver:
    :return:
    """
    task_name = util.generate_random_chars(0)
    driver.find_element(*TaskObjects.create_newtask).send_keys(task_name)
    driver.find_element(*TaskObjects.add_task_icon).click()
    todolist_table = driver.find_elements(*TaskObjects.task_table)
    for list in todolist_table:
        assert list.text != 'empty', "Task is created with empty characters"


def test_valid_task(driver):
    """
    Test task get created with valid input
    :param driver:
    :return:
    """
    task_name = util.generate_random_chars(5)
    driver.find_element(*TaskObjects.create_newtask).send_keys(task_name)
    driver.find_element(*TaskObjects.add_task_icon).click()
    todolist_table = driver.find_elements(*TaskObjects.task_table)
    task_list = []
    for list in todolist_table:
        task_list.append(list.text)

    assert task_name in task_list, "Task is not created"
    return task_name
