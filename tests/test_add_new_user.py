from pages.pim_page import TestAddNewUser


class TestAddUser:

    def test_add_new_user(self, login_and_open_dashboard):
        start_page = login_and_open_dashboard
        add_new_user_page = TestAddNewUser(driver=start_page.driver, url=start_page.url)
        add_new_user_page.add_new_user()
