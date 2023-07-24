from pages.main_page import MainPage
from locators.elements_login_page import StartPage


class LoginAction(MainPage):
    locators = StartPage

    def fill_fields_login(self):
        self.element_is_visible(self.locators.LOGIN).send_keys('Admin')
        self.element_is_visible(self.locators.PASSWORD).send_keys('admin123')
        self.element_is_visible(self.locators.LOGIN_BUTTON).click()
