import time

from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginAction

class TestDashboard:
    # Time at Work
    def test_widgets_taw(self, driver):
        login = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
        login.open()
        login.fill_fields_login()
        T_W_A = DashboardPage(driver, 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index')
        T_W_A.open()

        # Check if the widget's name is "Time at Work"
        widget_name = T_W_A.widget_t_a_w()
        assert widget_name == "Time at Work"

    # Test clicking on "Pending Self Review" link
    def test_click_pending_review_link(self, driver):
        login = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
        login.open()
        login.fill_fields_login()
        MA = DashboardPage(driver, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        MA.open()
        _, pending_review_link, _, _ = MA.widget_m_a()

        # Perform the click on "Pending Self Review" link
        pending_review_link.click()

        # Wait for the redirect to complete
        WebDriverWait(driver, 10).until(lambda
                                            d: d.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview")

        # Assert that the current URL is the expected URL
        assert driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview"

    # Test clicking on "Timesheets to Approve" link
    def test_click_timesheets_to_approve_link(self, driver):
        login = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
        login.open()
        login.fill_fields_login()
        MA = DashboardPage(driver, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        MA.open()
        _, _, timesheets_url, _ = MA.widget_m_a()
        assert timesheets_url == "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"
        # Adding a delay after the click
        time.sleep(3)

    # Test clicking on "Candidates to Interview" link
    def test_click_candidates_to_interview_link(self, driver):
        login = LoginAction(driver, 'https://opensource-demo.orangehrmlive.com/')
        login.open()
        login.fill_fields_login()
        MA = DashboardPage(driver, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        MA.open()
        _, _, _, candidates_url = MA.widget_m_a()
        assert candidates_url == "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates?statusId=4"
        # Adding a delay after the click
        time.sleep(3)
