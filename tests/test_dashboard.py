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

    def test_candidates_to_interview_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        candidates_to_interview_link = DashboardPage.WidgetTWA(dashboard_page)
        CTI_link = candidates_to_interview_link.check_candidates_to_interview_link()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates?statusId=4"

        assert CTI_link == expected_url

    def test_leave_requests_to_approve_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        leave_requests_to_approve_link = DashboardPage.WidgetTWA(dashboard_page)
        LRTA_link = leave_requests_to_approve_link.check_leave_requests_to_approve_link()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"

        assert LRTA_link == expected_url

    # Quick Launch

    def test_quick_launch_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        quick_launch_widget = DashboardPage.QuickLaunchWidget(dashboard_page)
        QL_name = quick_launch_widget.check_element_name_ql()
        expected_name = 'Quick Launch'

        assert expected_name == QL_name

    def test_my_leave_button_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        my_leave_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        MLB_name = my_leave_button.check_my_leave_button_link()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList"
        assert expected_url == MLB_name

    def test_leave_list_button_link(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        leave_list_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        LLB_name = leave_list_button.check_leave_list_button_link()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList"

        assert LLB_name == expected_url

    def test_timesheets_button(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        timesheets_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        TB_button = timesheets_button.check_timesheets_button()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"

        assert TB_button == expected_url

    def test_apply_leave_button(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        apply_leave_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        ALB_link = apply_leave_button.check_apply_leave_button()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave"

        assert ALB_link == expected_url

    def test_assign_leave_button(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        assign_leave_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        ASLB_link = assign_leave_button.check_assign_leave_button()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave"

        assert ASLB_link == expected_url

    def test_my_timesheets_button(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        my_timesheets_button = DashboardPage.QuickLaunchWidget(dashboard_page)
        MTB_link = my_timesheets_button.check_my_timesheets_button()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet"

        assert MTB_link == expected_url

    # Buzz Latest Posts
    def test_BLP_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        BLP_widget_name = DashboardPage.widget_b_l_p(dashboard_page)
        expected_name = 'Buzz Latest Posts'

        assert BLP_widget_name == expected_name

    # Employees on Leave Today

    def test_EOLT_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        EOLT_widget_name = DashboardPage.widget_e_o_l_t(dashboard_page)
        expected_name = 'Employees on Leave Today'

        assert EOLT_widget_name == expected_name

    # Employee Distribution by Sub Unit

    def test_EDbSU_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        EDbSU_widget_name = DashboardPage.widget_e_d_b_s_u(dashboard_page)
        expected_name = 'Employee Distribution by Sub Unit'

        assert EDbSU_widget_name == expected_name

    # Employee Distribution by Location

    def test_EDBL_widget_name(self, login_and_open_dashboard):
        dashboard_page = login_and_open_dashboard
        EDBL_widget_name = DashboardPage.widget_e_d_b_l(dashboard_page)
        expected_name = 'Employee Distribution by Location'

        assert EDBL_widget_name == expected_name
