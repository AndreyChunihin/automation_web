from selenium.webdriver.common.by import By

photo_for_user = '/home/ac/Downloads/photo.jpeg'

class PimElements:
    class PipTab:
        PIP_TAB = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')

    class AddButton:
        ADD_BUTTON = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')

    class AddEmployeeForm:
        ADD_PHOTO_BUTTON = (
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button')

        FIRSTNAME = (By.CSS_SELECTOR,'input[name="firstName"]')
        MIDDLE_NAME = (By.CSS_SELECTOR,'input[name="middleName"]')
        LASTNAME = (By.CSS_SELECTOR,'input[name="lastName"]')
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
