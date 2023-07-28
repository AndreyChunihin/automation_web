import time

from locators.elements_pim_page import PimElements
from pages.main_page import MainPage


class TestAddNewUser(MainPage):
    locators = PimElements

    def add_new_user(self):
        self.find_element(self.locators.PipTab.PIP_TAB).click()
        self.find_element(self.locators.AddButton.ADD_BUTTON).click()
        employee_id_element = self.find_element(self.locators.AddEmployeeForm.EMPLOYEE_ID)
        employee_id_value = employee_id_element.get_attribute("value")
        self.find_element(self.locators.AddEmployeeForm.FIRSTNAME).send_keys('Andrey')
        self.find_element(self.locators.AddEmployeeForm.MIDDLE_NAME).send_keys('Qa')
        self.find_element(self.locators.AddEmployeeForm.LASTNAME).send_keys('QA')
        self.find_element(self.locators.AddEmployeeForm.SLIDER_LOGIN_DETAILS).click()
        self.find_element(self.locators.AddEmployeeForm.USERNAME).send_keys('AndreyQA')
        self.find_element(self.locators.AddEmployeeForm.PASSWORD).send_keys('123456a')
        self.find_element(self.locators.AddEmployeeForm.CONFIRM_PASSWORD).send_keys('123456a')
        self.find_element(self.locators.AddEmployeeForm.SAVE_BUTTON).click()
        # Wait for the element to be clickable before clicking
        self.element_is_visible(self.locators.EmployeeInformation.PERSONAL_DETAILS).click()
        self.element_is_visible(self.locators.EmployeeInformation.EMPLOYEE_LIST_TAB).click()
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_NAME_SEARCH_FIELD).send_keys('Andrey')

        # Wait for the element to be clickable before clicking
        self.element_is_visible(self.locators.EmployeeInformation.SEARCH_BUTTON).click()

        # Wait for the element to be clickable before clicking
        self.element_is_visible(self.locators.EmployeeInformation.EMPLOYEE_CARD).click()

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
        self.find_element(self.locators.EmployeeInformation.EMPLOYEE_NAME_SEARCH_FIELD).send_keys('Andrey')

        # Wait for the element to be clickable before clicking
        self.element_is_visible(self.locators.EmployeeCard.DELETE_BUTTON).click()

        # Wait for the element to be clickable before clicking
        self.element_is_visible(self.locators.EmployeeCard.YES_DELETE_BUTTON).click()
