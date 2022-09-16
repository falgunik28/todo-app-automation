
from selenium.webdriver.common.by import By


class TaskObjects:
    my_task = (By.ID, "my_task")
    heading = (By.TAG_NAME, "h1")
    add_task_icon = (By.CLASS_NAME, "input-group-addon")
    task_row=(By.CSS_SELECTOR,"table>tbody>tr")
    manage_subtask_btn = (By.CLASS_NAME, "btn-primary")
    remove_task_btn = (By.CLASS_NAME, "btn-danger")
    task_table = (By.CSS_SELECTOR, ".table td a")    # .task_body- this is task name
    sign_in = (By.CSS_SELECTOR, "#sign_in")
    # navigation_bar = (By.CLASS_NAME, ".navbar-toggle")
    user_email = (By.ID, "user_email")
    user_pwd = (By.ID,"user_password")
    sign_in_btn = (By.CLASS_NAME, "btn-primary")
    create_newtask = (By.ID, "new_task")



