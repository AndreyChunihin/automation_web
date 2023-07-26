import time

import pyautogui as pyautogui

from pages.main_page import MainPage
from locators.elements_pim_page import PimElements,photo_for_user


class TestAddNewUser(MainPage):
    locators = PimElements

    def add_new_user(self):
        self.find_element(self.locators.PipTab.PIP_TAB).click()
        time.sleep(2)
        self.find_element(self.locators.AddButton.ADD_BUTTON).click()
        time.sleep(2)
        upload_button = self.find_element(self.locators.AddEmployeeForm.ADD_PHOTO_BUTTON)
        upload_button.click()
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.FIRSTNAME).send_keys('Andrey')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.MIDDLE_NAME).send_keys('Qa')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.LASTNAME).send_keys('QA')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.EMPLOYEE_ID).clear()
        self.find_element(self.locators.AddEmployeeForm.EMPLOYEE_ID).send_keys('2222')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.SLIDER_LOGIN_DETAILS).click()
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.USERNAME).send_keys('AndreyQA')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.PASSWORD).send_keys('123456a')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.CONFIRM_PASSWORD).send_keys('123456a')
        time.sleep(3)
        self.find_element(self.locators.AddEmployeeForm.SAVE_BUTTON).click()
