import time

import pyautogui as pyautogui

from locators.elements_pim_page import PimElements
from pages.main_page import MainPage


class TestAddNewUser(MainPage):
    locators = PimElements

    def add_new_user(self):
        self.find_element(self.locators.PipTab.PIP_TAB).click()
        self.find_element(self.locators.AddButton.ADD_BUTTON).click()
        upload_button = self.find_element(self.locators.AddEmployeeForm.ADD_PHOTO_BUTTON)
        upload_button.click()
        time.sleep(1)
        pyautogui.click(913, 484)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        pyautogui.write('photo.jpeg')
        time.sleep(3)
        pyautogui.click(1008, 687)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(1)
        employee_id_element = self.find_element(self.locators.AddEmployeeForm.EMPLOYEE_ID)
        employee_id_value = employee_id_element.get_attribute("value")
        time.sleep(1)
        self.find_element(self.locators.AddEmployeeForm.FIRSTNAME).send_keys('Andrey')
        self.find_element(self.locators.AddEmployeeForm.MIDDLE_NAME).send_keys('Qa')
        self.find_element(self.locators.AddEmployeeForm.LASTNAME).send_keys('QA')
        self.find_element(self.locators.AddEmployeeForm.SLIDER_LOGIN_DETAILS).click()
        self.find_element(self.locators.AddEmployeeForm.USERNAME).send_keys('AndreyQA')
        self.find_element(self.locators.AddEmployeeForm.PASSWORD).send_keys('123456a')
        self.find_element(self.locators.AddEmployeeForm.CONFIRM_PASSWORD).send_keys('123456a')
        self.find_element(self.locators.AddEmployeeForm.SAVE_BUTTON).click()
        time.sleep(2)
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_LIST_TAB).click()
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_LIST_FIELD).send_keys(employee_id_value)
        time.sleep(1)
        self.find_element(self.locators.EmployeeInformation.SEARCH_BUTTON).click()
        time.sleep(2)
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_CARD).click()
        return employee_id_value

    def check_user_card_field(self):
        created_username_element = self.find_element(self.locators.EmployeeCard.CREATED_USERNAME)
        created_middle_name_element = self.find_element(self.locators.EmployeeCard.CREATED_MIDDLE_NAME)
        created_lastname_element = self.find_element(self.locators.EmployeeCard.CREATED_LASTNAME)
        created_user_id_element = self.find_element(self.locators.EmployeeCard.EMPLOYEE_ID)

        created_username = created_username_element.get_attribute("value")
        created_middle_name = created_middle_name_element.get_attribute("value")
        created_lastname = created_lastname_element.get_attribute("value")
        created_user_id = created_user_id_element.get_attribute("value")

        return created_username, created_middle_name, created_lastname, created_user_id

    def delete_user(self, employee_id_value):
        self.find_element(self.locators.PipTab.PIP_TAB).click()
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_LIST_FIELD).send_keys(employee_id_value)
        time.sleep(3)
        self.find_element(self.locators.EmployeeCard.DELETE_BUTTON).click()
        time.sleep(3)
        self.find_element(self.locators.EmployeeCard.YES_DELETE_BUTTON).click()
