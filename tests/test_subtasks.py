import pytest
from selenium.common.exceptions import NoSuchElementException

from pages.subtask_page import SubTask_Objects
from pages.task_page import TaskObjects
from utils.utility import Util

util = Util()


def create_task(driver):
    """
    utility method to create new task
    :param driver:
    :return: task_name
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


def open_manage_subtask(driver, task_name):
    """
    Utility method to open subtask of any task
    :param driver:
    :param task_name:
    """
    todolist_table = driver.find_elements(*TaskObjects.task_row)
    for list in todolist_table:
        if task_name in list.text:
            list.find_element(*TaskObjects.manage_subtask_btn).click()


def test_empty_subtask_with_no_duedate(driver):
    """
    Test if subtask and due dates are mandatory
    :param driver:
    :return:
    """
    task = create_task(driver)
    open_manage_subtask(driver, task)

    # removing the due date to make it empty
    driver.find_element(*SubTask_Objects.duedate).clear()
    driver.find_element(*SubTask_Objects.add_subtask).click()
    subtask_list = driver.find_elements(*SubTask_Objects.subtask_names)
    sub_task_list = []
    for list in subtask_list:
        sub_task_list.append(list.text)
    driver.find_element(*SubTask_Objects.subtask_close_btn).click()
    assert 'empty' not in sub_task_list, "Sub Task is created with empty description"


@pytest.mark.parametrize('invalid_duedate,subtask_created',
                         [("abc", 0), ("99-00-22", 0), ("2022-02-02", 0), ("30/12/2023", 0)])
def test_duedate_value(driver, invalid_duedate, subtask_created):
    """
    Test date field should not accept any character or format.
    :param driver:
    :param invalid_duedate:
    :param subtask_created:
    :return:
    """
    task = create_task(driver)
    open_manage_subtask(driver, task)
    driver.find_element(*SubTask_Objects.duedate).clear()
    driver.find_element(*SubTask_Objects.duedate).send_keys(invalid_duedate)
    driver.find_element(*SubTask_Objects.add_subtask).click()
    subtask_list = []
    try:
        subtask_list = driver.find_elements(*SubTask_Objects.subtask_names)
    except NoSuchElementException:
        pass
    driver.find_element(*SubTask_Objects.subtask_close_btn).click()
    assert len(subtask_list) == subtask_created, "Subtask is created with random character in duedate"


def test_subtask_name_morethan_250(driver):
    """
    Test subtask accepts only 250 characters
    :param driver:
    :return:
    """
    task = create_task(driver)
    open_manage_subtask(driver, task)
    subtask_name = util.generate_random_chars(253)
    driver.find_element(*SubTask_Objects.subtask_desc).send_keys(subtask_name)
    driver.find_element(*SubTask_Objects.add_subtask).click()
    subtask_list = driver.find_elements(*SubTask_Objects.subtask_names)
    task_list = []
    for list in subtask_list:
        task_list.append(list.text)
    driver.find_element(*SubTask_Objects.subtask_close_btn).click()
    assert subtask_name not in task_list, "Sub Task is created with more than 250 characters"
