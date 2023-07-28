from pages.pim_page import TestAddNewUser

class TestAddUser:

    def test_add_new_user(self, login_and_open_dashboard):
        start_page = login_and_open_dashboard
        add_new_user_page = TestAddNewUser(driver=start_page.driver, url=start_page.url)

        employee_id_value = None

        try:
            employee_id_value = add_new_user_page.add_new_user()
            created_username, created_middle_name, created_lastname, created_user_id = add_new_user_page.check_user_card_field()

            expected_first_name = 'Andrey'
            expected_middle_name = 'Qa'
            expected_last_name = 'QA'

            assert expected_first_name == created_username
            assert expected_middle_name == created_middle_name
            assert expected_last_name == created_lastname
            assert employee_id_value == created_user_id

        finally:

            if employee_id_value is not None:
                add_new_user_page.delete_user(employee_id_value)
