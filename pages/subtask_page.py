from selenium.webdriver.common.by import By


class SubTask_Objects:
    modal_popup_page = (By.CLASS_NAME, ".modal-dialog")
    modal_heading = (By.TAG_NAME, "h3")
    task_desc = (By.ID, "edit_task")
    subtask_desc = (By.ID, "new_sub_task")
    duedate = (By.ID, "dueDate")
    add_subtask = (By.ID, "add-subtask")
    subtask_close_btn = (By.CSS_SELECTOR, ".modal-footer .btn")
    subtask_names=(By.CSS_SELECTOR,'.modal-body table tbody a')

