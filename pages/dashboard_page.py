from pages.main_page import MainPage
from locators.elements_dashboar_page import DashboardWidgets


class DashboardPage(MainPage):
    locators = DashboardWidgets

    # Time at Work
    def widget_t_a_w(self):
        widget_element = self.find_element(self.locators.TimeAtWorkWidget.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name

        # My Actions

    class WidgetTWA:
        def __init__(self, parent):
            self.parent = parent

        def check_widget_name(self):
            widget_element = self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.WIDGET_NAME)
            widget_name = widget_element.text
            return widget_name

        def pending_self_review(self):
            self.parent.element_is_visible(self.parent.locators.MyActionsWIDGET.
                                           PENDING_SELF_REVIEW).click()
            # return url for assert
            return self.parent.driver.current_url

        def check_timesheets_to_approve_link(self):
            self.parent.find_element(self.parent.locators.MyActionsWIDGET.TIMESHEETS_TO_APPROVE).click()
            return self.parent.driver.current_url

        def check_candidates_to_interview_link(self):
            self.parent.find_element(self.parent.locators.MyActionsWIDGET.CANDIDATES_TO_INTERVIEW).click()
            return self.parent.driver.current_url

        def check_leave_requests_to_approve_link(self):
            self.parent.find_element(self.parent.locators.MyActionsWIDGET.LEAVE_REQUESTS_TO_APPROVE).click()
            return self.parent.driver.current_url

        # Quick Launch

    class QuickLaunchWidget:

        def __init__(self, parent):
            self.parent = parent

        def check_element_name_ql(self):
            widget_element = self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.ELEMENT_QL)
            self.parent.scroll_to_element(widget_element)
            widget_name = widget_element.text
            return widget_name

        def check_my_leave_button_link(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.MY_LEAVE_BUTTON).click()
            return self.parent.driver.current_url

        def check_leave_list_button_link(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.LEAVE_LIST_BUTTON).click()
            return self.parent.driver.current_url

        def check_timesheets_button(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.TIMESHEETS_BUTTON).click()
            return self.parent.driver.current_url

        def check_apply_leave_button(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.APPLY_LEAVE_BUTTON).click()
            return self.parent.driver.current_url

        def check_assign_leave_button(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.ASSIGN_LEAVE_BUTTON).click()
            return self.parent.driver.current_url

        def check_my_timesheets_button(self):
            self.parent.find_element(self.parent.locators.QuickLaunchWIDGET.MY_TIMESHEETS_BUTTON).click()
            return self.parent.driver.current_url

        # Buzz Latest Posts

    def widget_b_l_p(self):
        widget_element = self.find_element(self.locators.BuzzLatestPosts.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name

        # Employees on Leave Today

    def widget_e_o_l_t(self):
        widget_element = self.find_element(self.locators.EmployeesOnLeaveToday.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name

        # Employee Distribution by Sub Unit

    def widget_e_d_b_s_u(self):
        widget_element = self.find_element(self.locators.EmployeeDistributionBySubUnit.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name

        # Employee Distribution by Location

    def widget_e_d_b_l(self):
        widget_element = self.find_element(self.locators.EmployeeDistributionByLocation.WIDGET_NAME)
        widget_name = widget_element.text
        return widget_name
