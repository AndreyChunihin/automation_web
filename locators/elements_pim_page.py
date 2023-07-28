from selenium.webdriver.common.by import By

photo_for_user = '/home/ac/PycharmProjects/automation_web_V3/for_test_staff/photo.jpeg'


class PimElements:
    class PipTab:
        PIP_TAB = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')

    class AddButton:
        ADD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')

    class AddEmployeeForm:
        ADD_PHOTO_BUTTON = (
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button')

        FIRSTNAME = (By.CSS_SELECTOR, 'input[name="firstName"]')
        MIDDLE_NAME = (By.CSS_SELECTOR, 'input[name="middleName"]')
        LASTNAME = (By.CSS_SELECTOR, 'input[name="lastName"]')
        EMPLOYEE_ID = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div['
                                 '2]/div/div/div[2]/input')

        SLIDER_LOGIN_DETAILS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]'
                                          '/div[2]/div/label/span')

        USERNAME = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]'
                              '/div/div[1]/div/div[2]/input')
        ENABLED = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]'
                             '/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span')
        DISABLED = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]'
                              '/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span')
        PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]'
                              '/div[2]/div[4]/div/div[1]/div/div[2]/input')
        CONFIRM_PASSWORD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div'
                                      '[1]/div[2]/div[4]/div/div[2]/div/div[2]/input')

        CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]')

        SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')

        EMPLOYEE_LIST_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')

    class EmployeeInformation:
        PERSONAL_DETAILS = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a')
        EMPLOYEE_LIST_TAB = (By.CSS_SELECTOR, '#app header nav ul li:nth-child(2) a')
        EMPLOYEE_LIST_FIELD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div['
                                         '2]/div/div[2]/input')
        EMPLOYEE_NAME_SEARCH_FIELD = (
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]'
                      '/div/div[2]/div/div/input')
        SEARCH_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')
        EMPLOYEE_CARD = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div')

    class EmployeeCard:
        CREATED_USERNAME = (By.CSS_SELECTOR, '.oxd-input.oxd-input--active.orangehrm-firstname')
        CREATED_MIDDLE_NAME = (By.CSS_SELECTOR, '.oxd-input.oxd-input--active.orangehrm-middlename')
        CREATED_LASTNAME = (By.CSS_SELECTOR, '.oxd-input.oxd-input--active.orangehrm-lastname')
        EMPLOYEE_ID = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div'
                                 '/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        DELETE_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]'
                                   '/div/div[2]/div/div/div[9]/div/button[1]')
        YES_DELETE_BUTTON = (By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
