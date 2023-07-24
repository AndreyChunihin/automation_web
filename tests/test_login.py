import time
from pages.login_page import LoginAction


class TestLogin:
    def test_login_in_app(self, driver):
        login_in_app = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
        login_in_app.open()
        login_in_app.fill_fields_login()
        time.sleep(4)
        current_url = driver.current_url
        expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        assert current_url == expected_url



