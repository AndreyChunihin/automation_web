import time

from pages.dashboard_page import DashboardPage


class TestDashboard:
    # Time at Work
    def test_widgets_taw(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        widget_name = dashboard_page.widget_t_a_w()
        assert widget_name == "Time at Work"

    # Test clicking on "Pending Self Review" link
    def test_widget_PSRL_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        widget_twa = dashboard_page.WidgetTWA(dashboard_page)
        assert widget_twa.check_widget_name() == 'My Actions'

    def test_pending_self_review_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        widget_twa = dashboard_page.WidgetTWA(dashboard_page)
        pending_self_review_url = widget_twa.pending_self_review()
        expected_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/performance/myPerformanceReview'

        assert pending_self_review_url == expected_url

    def test_timesheets_to_approve_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        TTA_link = dashboard_page.WidgetTWA(dashboard_page)
        timesheets_to_approve_link = TTA_link.check_timesheets_to_approve_link()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"

        assert timesheets_to_approve_link == expected_url

        #Quick Launch

    def test_quick_launch_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        quick_launch_widget = DashboardPage.QuickLaunchWidget(dashboard_page)
        QL_name = quick_launch_widget.check_element_name_ql()
        expected_name = 'Quick Launch'

        assert expected_name == QL_name


